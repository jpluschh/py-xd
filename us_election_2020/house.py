#! /usr/bin/python3

import pandas as pd


hr_cand        = pd.read_csv('./raw/house_candidate.csv')
hr_state       = pd.read_csv('./raw/house_state.csv')

print(hr_cand.info())
print(hr_cand.describe())
print(hr_state.info())
print(hr_state.describe())

