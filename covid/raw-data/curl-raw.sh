#! /usr/bin/bash

backup_dir=$(date +'%Y%m%d')
mkdir $backup_dir
curl -o $backup_dir/owid-covid-data.csv https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv
curl -o $backup_dir/owid-covid-data.json https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.json
