#! /usr/bin/python3

import pandas as pd


sen_cnty       = pd.read_csv('./raw/senate_county.csv')
sen_cnty_cand  = pd.read_csv('./raw/senate_county_candidate.csv')
sen_state      = pd.read_csv('./raw/senate_state.csv')

print(sen_cnty.info())
print(sen_cnty.describe())
print(sen_cnty_cand.info())
print(sen_cnty_cand.describe())
print(sen_state.info())
print(sen_state.describe())

