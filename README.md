# DATA_ENGINEERING_PROJ
## DATA DESCRIPTION
DATA is list of crimes which were comitted in New-York from 2020 till present.
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
 
