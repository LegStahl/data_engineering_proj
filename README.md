# DATA_ENGINEERING_PROJ
## CONFIGURING
In this project manager miniconda is used.
File requirements.txt contains all required components to run program. 
By using miniconda you can easily download all.
1. `conda create --name <your_project_name> //By this line you crated virtula env with that name
2. `conda activate <your_project_name>//By this line you activate your created virual env
3. `conda config --add channels conda-forge//one library gdown which is required to download big files from google drive requires another source
4. `conda install --yes --file requirements.txt //By this line you install all dependencies
5. `conda deactivate//By this line of code you disable your virtual env

##ENABLE ETL SCRIPT
` python3 data_load.py
Link to the data: https://drive.google.com/file/d/1wzoyCfrIO56nn9r0DoqQdStargKmDUKu/view?usp=drive_link

<p align="center">First 10 lines of data</p>
![FIRST 10 lines of data](images/screenshot.png)
 
