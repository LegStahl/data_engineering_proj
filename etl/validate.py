import pandas as pd


def data_validation(df):
    cols_to_drop = ["Cross_Street", "Weapon_Desc", "Mocodes"]
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
    return df
