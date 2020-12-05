# plot

import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#import excel
stock_day_2020 = pd.read_excel('stock_day_2020_clean.xlsx', sheet_name='2020')

# ROC to Gregorian
for i in range(len(stock_day_2020['Dates'])):
    y, m, d = stock_day_2020.iloc[i,0].split('/')
    stock_day_2020.iloc[i,0] = str(int(y)+1911) + '/' + m + '/' + d

stock_day_2020['Date'] = pd.to_datetime(stock_day_2020['Dates'])
stock_day_2020.set_index('Date', inplace=True)


x = stock_day_2020['Dates']
y1 = stock_day_2020['High']
y2 = stock_day_2020['Low']
y3 = stock_day_2020['Open']
y4 = stock_day_2020['Close']
y5 = stock_day_2020['Diff'].str.replace('X0.00', '0', regex=False)
# y6 = stock_day_2020['Turnover']

'''
# testing different plots
graph = plt.plot(x, y1, x, y2, x, y3, x, y4, x, y5)
plt.setp(graph[0], linewidth=1)
plt.setp(graph[1], linewidth=2)
plt.setp(graph[2], linewidth=3)
plt.setp(graph[3], linewidth=4)
plt.setp(graph[4], linewidth=5)

# set legend
plt.legend(('Open', 'High', 'Low', 'Close', 'Diff'),
           loc='upper right')

stock_day_2020.plot(x="Date",
                    y="Open", "High", "Low", "Close", "Diff", "Turnover",
                    alpha=0.5)
'''


# Figuring out gridspec
fig = plt.figure()
gs = gridspec.GridSpec(2, 2)
#gs = gridspec.GridSpec(3, 2)


ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(y1)
ax1.set_ylabel('High')
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(y2)
ax2.set_ylabel('Low')
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(y3)
ax3.set_ylabel('Open')
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(y4)
ax4.set_ylabel('Close')
#ax5 = fig.add_subplot(gs[2, :])
#ax5.plot(y5)
#ax5.set_ylabel('Diff')


# set title
fig.suptitle('TSMC 2330')

# fix date annoyance
fig.autofmt_xdate()

# fix spacing
fig.tight_layout()

# save plot
plt.savefig('2330-grid.png', dpi=2000)
