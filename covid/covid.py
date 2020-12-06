#! /usr/bin/python3

import pandas as pd
#import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('./raw-20201206/owid-covid-data.csv')

#viz - icu patients per million
icu_ppm_filtered = df[df['icu_patients_per_million'] > 0]
icu_ppm_x = icu_ppm_filtered['location']
icu_ppm_y = icu_ppm_filtered['icu_patients_per_million'].sort_values()


#viz - hosp patients per million
hosp_ppm_filtered = df[df['hosp_patients_per_million'] > 0]
hosp_ppm_x = hosp_ppm_filtered['location']
hosp_ppm_y = hosp_ppm_filtered['hosp_patients_per_million'].sort_values()


fig, (ax1, ax2) = plt.subplots(1,2)
ax1.barh(icu_ppm_x,icu_ppm_y)
ax1.set_title('icu patients per million')
ax2.barh(hosp_ppm_x,hosp_ppm_y)
ax2.set_title('hosp patients per million')

#ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
fig.tight_layout()

# save plot
plt.savefig('hosp_icu_ppmv.png', dpi=1000)



