#! /usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./raw-data/20201207-europa/data.csv')

# date time data type parsing practice
#df['dateRep_parsed'] = pd.to_datetime(df['dateRep'], format="%d/%m/%Y")

plt.scatter(df['month'], df['cases'])


# save plot
plt.savefig('month.png', dpi=1000)


