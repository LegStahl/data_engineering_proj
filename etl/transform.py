import  pandas as pd
import validate

RENAME_DICT = {
    "DR NO": "DR_NO", #
    "Date Rptd": "Date_Rptd",#
    "DATE OCC": "DATE_OCC",#
    "TIME OCC": "TIME_OCC",
    "AREA NAME": "AREA_NAME",
    "Rpt Dist No": "Rpt_Dist_No",
    "Part 1-2": "Part_1_2",
    "Crm Cd": "Crm_Cd",
    "Crm Cd Desc": "Crm_Cd_Desc",
    "Mocodes": "Mocodes",
    "Vict Age": "Vict_Age",
    "Vict Sex": "Vict_Sex",
    "Vict Descent": "Vict_Descent",
    "Premis Cd": "Premis_Cd",
    "Premis Desc": "Premis_Desc",
    "Weapon Used Cd": "Weapon_Used_Cd",
    "Weapon Desc": "Weapon_Desc",
    "Status": "Status",
    "Status Desc": "Status_Desc",
    "Crm Cd 1": "Crm_Cd_1",
    "Crm Cd 2": "Crm_Cd_2",
    "Crm Cd 3": "Crm_Cd_3",
    "Crm Cd 4": "Crm_Cd_4",
    "LOCATION": "LOCATION",
    "Cross Street": "Cross_Street",
    "LAT": "LAT",
    "LON": "LON"
}


def transform_int_and_float(df):
    cols_to_int = ["Crm_Cd_1", "Crm_Cd_2", "Crm_Cd_3", "Crm_Cd_4", "Premis_Cd", "Weapon_Used_Cd", "DR_NO", "AREA", "Rpt_Dist_No", "Part_1_2", "Vict_Age", "TIME_OCC"]
    for col in cols_to_int:
        if col in df.columns:
            df[col] = df[col].fillna(-1).astype(int)

    geo_cols = ["LAT", "LON"]
    for col in geo_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def transform_dates(df):
    date_format = "%m/%d/%Y %I:%M:%S %p"
    df['Date_Rptd'] = pd.to_datetime(df['Date_Rptd'],  format=date_format, errors='coerce').dt.date
    df['DATE_OCC'] = pd.to_datetime(df['DATE_OCC'], format=date_format, errors='coerce').dt.date
    return df

def transform_str(df):
    str_cols = ["AREA_NAME", "Crm_Cd_Desc", "Mocodes", "Premis_Desc",
            "Weapon_Desc", "Status_Desc", "LOCATION", "Cross_Street", "Vict_Sex", "Vict_Descent", "Status"]
    for col in str_cols:
        if col in df.columns:
            df[col] = df[col].astype("object")
    return df



def transform_data(df):
    df = df.rename(columns = RENAME_DICT)
    df = transform_int_and_float(df)
    df = transform_dates(df)
    df = transform_str(df)
    df = validate.data_validation(df)
    return df
