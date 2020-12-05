# histogram

import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#import excel
stock_day_2020 = pd.read_excel('stock_day_2020_clean.xlsx', sheet_name='2020')

# ROC to Gregorian
for i in range(len(stock_day_2020['Dates'])):
    y, m, d = stock_day_2020.iloc[i,0].split('/')
    stock_day_2020.iloc[i,0] = str(int(y)+1911) + '/' + m + '/' + d


x = stock_day_2020['Dates']
#y1 = stock_day_2020['High']
#y2 = stock_day_2020['Low']
#y3 = stock_day_2020['Open']
#y4 = stock_day_2020['Close']
y5 = stock_day_2020['Diff'].str.replace('X0.00', '0', regex=False).fillna(0)
#y6 = stock_day_2020['Turnover']

fig = plt.figure(tight_layout=True)
ax = fig.add_subplot(111)
ax.plot(x, y5)
ax.set_xlabel('Date', fontsize=14, fontweight='bold')
ax.set_ylabel('Diff', fontsize=14, fontweight='bold')
# TODO: fix xticks format


# set title
fig.suptitle('TSMC 2330')

# fix date annoyance
fig.autofmt_xdate()

# save plot
plt.savefig('2330-diff-hist.png', dpi=2000)
