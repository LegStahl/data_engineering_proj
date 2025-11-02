import gdown
import pandas as pd


OUTPUT = "RAW_DATA.csv"


def download_data(FILE_ID):
    print("Downloading data from google has started")
    file_url = f"https://drive.google.com/uc?id={FILE_ID}"
    result = gdown.download(file_url, OUTPUT, quiet=False)
    if result is not None:
        print("Download successful", result)
        raw_data = pd.read_csv(OUTPUT)
        return raw_data
    else:
        print("Download failed")
        return None
