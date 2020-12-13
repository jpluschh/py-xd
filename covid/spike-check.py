#! /usr/bin/python3

# Found a data spike in new cases graph in Asia.
# Wanted to double check if there's something wrong with the data or script.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./raw-data/20201214/owid-covid-data.csv')

asia = df.loc[(df.continent == 'Asia') & (df.new_cases > 5000)]

print(asia.info())
print(asia.describe())

# max value
print(asia['new_cases'].max())
# index of max value
print(asia['new_cases'].idxmax())
# print dataframe by index
print(asia.loc[57322])

