#! /usr/bin/python3

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

us_df = pd.read_csv('./1976-2018-senate.csv', encoding = 'utf-8')

x = us_df['year']
y = us_df['candidatevotes']

fig, ax = plt.subplots()
ax.bar(x,y)
ax.set_title('candidate votes')
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
fig.tight_layout()

# save plot
plt.savefig('votes.png', dpi=1000)

