from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData, select, text, inspect,  Column, Integer, String, Date, Time, Enum
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from sqlalchemy.engine import URL
from sqlalchemy.types import DateTime
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import os



Base = declarative_base()
PATH_TO_DATA = "crime_data.parquet"
BD_NAME_TEST = "freezone"
BD_NAME_HOMEWORK = "homeworks"
TABLE_NAME = "shtele"

class DRTable(Base):
    __tablename__ = TABLE_NAME

    DR_NO = Column(BIGINT, primary_key=True)
    Date_Rptd = Column(VARCHAR(50))
    DATE_OCC = Column(VARCHAR(50))
    TIME_OCC = Column(Integer)
    AREA = Column(Integer)
    AREA_NAME = Column(VARCHAR(100))
    Rpt_Dist_No = Column(Integer)
    Part_1_2 = Column(Integer)
    Crm_Cd_Desc = Column(VARCHAR(255))
    Vict_Age = Column(Integer)
    Vict_Sex = Column(Enum('M','F','X','U', name='vict_sex'))  # U = unknown
    Vict_Descent = Column(VARCHAR(50))  # category, можно ENUM
    Premis_Cd = Column(Integer)
    Premis_Desc = Column(VARCHAR(255))
    Weapon_Used_Cd = Column(Integer)
    Status = Column(VARCHAR(50))  # category, можно ENUM
    Status_Desc = Column(VARCHAR(255))
    LOCATION = Column(VARCHAR(255))

def read_from_parquet_100():

    df = pd.read_parquet(PATH_TO_DATA, engine="pyarrow")
    df_reduced = df.head(100).copy()
    date_format = "%m/%d/%Y %I:%M:%S %p"



    df_reduced['Date_Rptd'] = pd.to_datetime(df_reduced['Date_Rptd'],  format=date_format, errors='coerce').dt.date
    df_reduced['DATE_OCC'] = pd.to_datetime(df_reduced['DATE_OCC'], format=date_format, errors='coerce').dt.date

    categorical_cols = ['Vict_Sex', 'Vict_Descent', 'Status']
    for col in categorical_cols:
        df_reduced[col] = df_reduced[col].astype(str)

    for col in ['Vict_Sex', 'Vict_Descent', 'Status']:
        df_reduced[col] = df_reduced[col].where(df[col].notna(), None)

    return df_reduced

def work_with_db():
    user = os.getenv("DB_USER")
    password_ = os.getenv("DB_PASS")
    ip_addr = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    metadata = MetaData()
    db_choosing = input("would you like training of no DB?'yes' or 'no'")
    chose = 0
    if db_choosing == 'yes':
        chose = BD_NAME_TEST
    else:
        chose = BD_NAME_HOMEWORK

    url = URL.create(
        "postgresql+psycopg2",
        username=user,
        password=password_,
        host=ip_addr,
        port=int(port),
        database=chose
    )

    engine = create_engine(url)
    inspector = inspect(engine)

    schemas = inspector.get_schema_names()

    print("All schemas:")
    for schema in schemas:
        print(schema)

    tables = inspector.get_table_names(schema='public')
    print("All tables in public:")
    check = False
    for t in tables:
        if t == TABLE_NAME:
            check = True
        print(t)
    df = read_from_parquet_100()
    if not check:
        print("Table was created!")
        Base.metadata.create_all(engine)

    choosing = input("would you like to add 100 lines to db? 'yes' or 'no'")
    if choosing == 'yes':
        df.to_sql(
            TABLE_NAME,
            engine,
            if_exists='append',
            index=False
        )
    metadata = MetaData()
    metadata.reflect(bind=engine, schema='public')  # важно!
    dr_table = metadata.tables[f'public.{TABLE_NAME}']


    with engine.connect() as conn:
        result = conn.execute(select(dr_table))
        rows = result.fetchall()

    for row in rows:
        print(dict(row._mapping))


    engine.dispose()



def main():
 work_with_db()


if __name__ == "__main__":
    main()
