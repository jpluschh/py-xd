#! /usr/bin/python3

import pandas as pd


gov_cnty       = pd.read_csv('./raw/governors_county.csv')
gov_cnty_cand  = pd.read_csv('./raw/governors_county_candidate.csv')
gov_state      = pd.read_csv('./raw/governors_state.csv')

print(gov_cnty.info())
print(gov_cnty.describe())
print(gov_cnty_cand.info())
print(gov_cnty_cand.describe())
print(gov_state.info())
print(gov_state.describe())

