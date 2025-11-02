import os

import pandas as pd
from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    create_engine,
    MetaData,
    select,
    text,
    inspect,
    Column,
    Integer,
    String,
    Date,
    Time,
    Enum,
)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from sqlalchemy.engine import URL
from sqlalchemy.types import DateTime
from sqlalchemy.exc import SQLAlchemyError
import main

Base = declarative_base()

NAME_OF_DATA = "PROCESSED_DATA.parquet"
BD_NAME_TEST = "freezone"
BD_NAME_HOMEWORK = "homeworks"
TABLE_NAME = os.getenv("TABLE_NAME")
PUBLIC = "public"


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
    Vict_Sex = Column(Enum("M", "F", "X", "U", name="vict_sex"))
    Vict_Descent = Column(VARCHAR(50))
    Premis_Cd = Column(Integer)
    Premis_Desc = Column(VARCHAR(255))
    Weapon_Used_Cd = Column(Integer)
    Status = Column(VARCHAR(50))
    Status_Desc = Column(VARCHAR(255))
    LOCATION = Column(VARCHAR(255))


def get_engine_and_inspector(choosing):
    user = os.getenv("DB_USER")
    password_ = os.getenv("DB_PASS")
    ip_addr = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    metadata = MetaData()
    base_name = 0
    if choosing == main.DB_CHOOSING.test:
        base_name = BD_NAME_TEST
    else:
        base_name = BD_NAME_HOMEWORK
    url = URL.create(
        "postgresql+psycopg2",
        username=user,
        password=password_,
        host=ip_addr,
        port=int(port),
        database=base_name,
    )
    engine = create_engine(url)
    inspector = inspect(engine)
    return engine, inspector


def creating_table(engine, inspector):
    tables = inspector.get_table_names(schema="public")
    check = False
    print(TABLE_NAME)
    for t in tables:
        if t == TABLE_NAME:
            check = True
    print("Table was created!!!")
    print(check)
    Base.metadata.create_all(engine)
    return check


def add_data_to_db(df):
    df.to_sql(TABLE_NAME, engine, if_exists="append", index=False)
    metadata = MetaData()
    metadata.reflect(bind=engine, schema=PUBLIC)
    dr_table = metadata.tables[f"{PUBLIC}.{TABLE_NAME}"]
    try:
        with engine.connect() as conn:
            result = conn.execute(select(dr_table))
            rows = result.fetchall()
            print("Query executed successfully!")
            return True
    except SQLAlchemyError as e:
        print("Query failed!", e)
        return False


def write_data_to_parquet(df):
    df.to_parquet(NAME_OF_DATA, index=False)


def load_data(df, choosing):
    engine, inspector = get_engine_and_inspector(choosing)
    if creating_table(engine, inspector) == True:
        result = True  # add_data_to_db(df)
        return result
    else:
        print("Table couldn't be created, please check data base")
        return False
