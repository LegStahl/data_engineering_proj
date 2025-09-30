# DATA_ENGINEERING_PROJ
## DATA DESCRIPTION
DATA is list of crimes which were comitted in New-York from 2020 till present.
| Old name of column | New name of column     | Type of data in pandas | Description |
|------------------|--------------------------|------------------------|-------------|
| DR_NO            | dr_no              | Int64               | Unique ID of case |
| Date Rptd        | date_reported      | datetime64[ns]      | Date of register in DB |
| DATE OCC         | date_occured       | datetime64[ns]      | Date of commiting crime |
| TIME OCC         | time_occured       | datetime.time       | Time of commiting crime (hours:minutes) |
| AREA             | area               | Int64               | Code of police district |
| AREA NAME        | area_name          | string              | Name of police district |
| Rpt Dist No      | report_dist_no     | Int64               | Report district number |
| Part 1-2         | part               | Int64               | Degree of severity (Part 1 or Part 2) |
| Crm Cd           | crime_code         | Int64               | Main code if crime |
| Crm Cd Desc      | crime_desc         | string              | Crime description |
| Mocodes          | mocodes            | string              | Code of methods commiting crime |
| Vict Age         | victim_age         | Int64               | Age victim |
| Vict Sex         | victim_sex         | string              | Sex victim (M/F/X) |
| Vict Descent     | victim_descent     | string              | Ethnos |
| Premis Cd        | premis_code        | float64             | Code of place commiting |
| Premis Desc      | premis_desc        | string              | Desc of place commiting|
| Weapon Used Cd   | weapon_code        | float64             | Code of weapon (if used) |
| Weapon Desc      | weapon_desc        | string              | Weapon descript |
| Status           | status             | string              | Code status |
| Status Desc      | status_desc        | string              | Description status |
| Crm Cd 1         | crime_code_1       | float64             | Additional code of crime №1 |
| Crm Cd 2         | crime_code_2       | float64             | Additional code of crime №2 |
| Crm Cd 3         | crime_code_3       | float64             | Additional code of crime №3 |
| Crm Cd 4         | crime_code_4       | float64             | Additional code of crime №4 |
| LOCATION         | location           | string              | Address and description of place crime commited |
| Cross Street     | cross_street       | string              | Cross street (if is there) |
| LAT              | latitude           | float64             | Latitude |
| LON              | longitude          | float64             | Longitude |

## CONFIGURING
In this project manager miniconda is used.
File requirements.txt contains all required components to run program. 
By using miniconda you can easily download all.
1. <pre> conda create --name <your_project_name> </pre> By this line you created virtual env with that name
2. <pre> conda activate <your_project_name> </pre> By this line you activate your created virutal env
3. <pre> conda config --add channels conda-forge </pre> One library "gdown" which is required to download big files from google drive requires another source
4. <pre> conda install --yes --file requirements.txt </pre> By this line you install all dependencies
5. <pre> conda deactivate </pre> By this line of code you disable your virtual env

## ENABLE ETL SCRIPT
<pre>python3 data_load.py</pre>

Link to the data: https://drive.google.com/file/d/1GAFf1P8SRlm_NM77FwquFAQw1YLF5jBo/view?usp=drive_link

<p align="center">First 10 lines of data</p>

![FIRST 10 lines of data](images/screenshot.png)
 
