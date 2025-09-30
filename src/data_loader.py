import gdown
import  pandas as pd

FILE_ID="1GAFf1P8SRlm_NM77FwquFAQw1YLF5jBo"

file_url=f"https://drive.google.com/uc?id={FILE_ID}"

#file_url= f"https://drive.usercontent.google.com/download?id={FILE_ID}"

output = "crime_data.csv"

gdown.download(file_url, output, quiet=False)





raw_data=pd.read_csv(output)

print(raw_data.dtypes)



# --- Rename columns ---
raw_data.columns = [
    "dr_no", "date_reported", "date_occured", "time_occured",
    "area", "area_name", "report_dist_no", "part",
    "crime_code", "crime_desc", "mocodes",
    "victim_age", "victim_sex", "victim_descent",
    "premis_code", "premis_desc",
    "weapon_code", "weapon_desc",
    "status", "status_desc",
    "crime_code_1", "crime_code_2", "crime_code_3", "crime_code_4",
    "location", "cross_street", "latitude", "longitude"
]

# --- Dates ---
raw_data["date_reported"] = pd.to_datetime(raw_data["date_reported"], errors="coerce")
raw_data["date_occured"] = pd.to_datetime(raw_data["date_occured"], errors="coerce")

# --- Time ---
raw_data["time_occured"] = (
    raw_data["time_occured"].astype(str).str.replace(r"\D", "", regex=True).str.zfill(4)
)
raw_data["time_occured"] = pd.to_datetime(
    raw_data["time_occured"], format="%H%M", errors="coerce"
).dt.time

# --- Number codes ---
int_cols = ["dr_no", "area", "report_dist_no", "part", "crime_code", "victim_age"]
for col in int_cols:
    raw_data[col] = pd.to_numeric(raw_data[col], errors="coerce").astype("Int64")

# --- Float numbers ---
float_cols = [
    "premis_code", "weapon_code",
    "crime_code_1", "crime_code_2", "crime_code_3", "crime_code_4",
    "latitude", "longitude"
]
for col in float_cols:
    raw_data[col] = pd.to_numeric(raw_data[col], errors="coerce")

# --- string ---
categorical_cols = [
    "area_name", "crime_desc", "mocodes", "victim_sex", "victim_descent",
    "premis_desc", "weapon_desc", "status", "status_desc",
    "location", "cross_street"
]
for col in categorical_cols:
    raw_data[col] = raw_data[col].astype("string")

# --- Сохраняем в Parquet ---
raw_data.to_parquet("crime_data.parquet", engine="pyarrow", index=False)
