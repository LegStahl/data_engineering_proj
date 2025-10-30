#!/bin/bash

if [ ! -f "settings" ]; then
  echo "Fail: file 'settings' has not been found!"
  exit 1
fi

source settings


if [ -z "$name_of_env" ]; then
  echo "Fail: name of virtual env'name_of_env' has not been set!"
  exit 1
fi


echo "Adding channel conda-forge..."
conda config --add channels conda-forge

echo "Creating virtual env: $name_of_env"
conda create -n "$name_of_env"


eval "$(conda shell.bash hook)"

echo "Enable enviroment: $name_of_env"
conda activate "$name_of_env"

if [ -f "requirements.txt" ]; then
  echo "Installing dependencies from requirements.txt."
  conda install --yes --file requirements.txt
  echo "Installing has been finished."
else
  echo "File requirements.txt has not been found."
  exit 1
fi

echo "Setting all service variables..."

vars_cmd=""
[ -n "$TABLE_NAME" ] && vars_cmd+="TABLE_NAME='$TABLE_NAME' "
[ -n "$DB_USER" ] && vars_cmd+="DB_USER='$DB_USER' "
[ -n "$DB_PASS" ] && vars_cmd+="DB_PASS='$DB_PASS' "
[ -n "$DB_HOST" ] && vars_cmd+="DB_HOST='$DB_HOST' "
[ -n "$DB_PORT" ] && vars_cmd+="DB_PORT='$DB_PORT' "

if [ -n "$vars_cmd" ]; then
  eval "conda env config vars set $vars_cmd"
  echo "Variables of env has been set:"
  echo "$vars_cmd"
else
  echo "Error has been occured during settings variables."
  exit 1
fi

echo "Virtual env '$name_of_env' ready print conda activate <your_name>."
