#! /usr/bin/python3

import pandas as pd
#import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('./raw-20201206/owid-covid-data.csv')

#icu patients per million viz
icu_ppm_filtered = df[df['icu_patients_per_million'] > 0]
x = icu_ppm_filtered['location']
y = icu_ppm_filtered['icu_patients_per_million'].sort_values()
fig, ax = plt.subplots()
ax.barh(x,y)
ax.set_title('icu patients per million')
#ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
fig.tight_layout()

# save plot
plt.savefig('icu_ppmv.png', dpi=1000)



