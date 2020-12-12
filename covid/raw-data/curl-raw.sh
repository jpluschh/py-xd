#! /usr/bin/bash

backup_dir=$(date +'%Y%m%d')
mkdir $backup_dir
curl -o $backup_dir/owid-covid-data.csv https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv
