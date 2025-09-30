#API FOR FINDING REPOS WITH SPECIFIED REQUEST
##INSTRUCTIONS
In this project manager miniconda is used.
File requirements.txt contains all required components to run program. 
By using miniconda you can easily download all.
1. <pre> conda create --name <your_project_name> </pre> By this line you created virtual env with that name
2. <pre> conda activate <your_project_name> </pre> By this line you activate your created virutal env
3. <pre> conda config --add channels conda-forge </pre> One library "gdown" which is required to download big files from google drive requires another source
4. <pre> conda install --yes --file requirements.txt </pre> By this line you install all dependencies
5. <pre> conda deactivate </pre> By this line of code you disable your virtual env

File set contains specified words which repo must contain
