import gdown
import  pandas as pd
#https://drive.google.com/file/d/1wzoyCfrIO56nn9r0DoqQdStargKmDUKu/view?usp=drive_link
FILE_ID="1wzoyCfrIO56nn9r0DoqQdStargKmDUKu"
#file_url=f"https://drive.google.com/file/d/{FILE_ID}/view?usp=drive_link"


file_url=f"https://drive.google.com/uc?id={FILE_ID}"

#file_url= f"https://drive.usercontent.google.com/download?id={FILE_ID}"

output = "crime_data.csv"

gdown.download(file_url, output, quiet=False)


raw_data=pd.read_csv(output)

print(raw_data.head(10))
