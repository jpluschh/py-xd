# Data cleanup

import pandas as pd

'''
jan = pd.read_csv('./raw/2330/STOCK_DAY_2330_202001.csv', header=0, encoding='big5')
feb = pd.read_csv('./raw/2330/STOCK_DAY_2330_202002.csv', header=0, encoding='big5')
mar = pd.read_csv('./raw/2330/STOCK_DAY_2330_202003.csv', header=0, encoding='big5')
apr = pd.read_csv('./raw/2330/STOCK_DAY_2330_202004.csv', header=0, encoding='big5')
may = pd.read_csv('./raw/2330/STOCK_DAY_2330_202005.csv', header=0, encoding='big5')
jun = pd.read_csv('./raw/2330/STOCK_DAY_2330_202006.csv', header=0, encoding='big5')
jul = pd.read_csv('./raw/2330/STOCK_DAY_2330_202007.csv', header=0, encoding='big5')
aug = pd.read_csv('./raw/2330/STOCK_DAY_2330_202008.csv', header=0, encoding='big5')
sep = pd.read_csv('./raw/2330/STOCK_DAY_2330_202009.csv', header=0, encoding='big5')
oct = pd.read_csv('./raw/2330/STOCK_DAY_2330_202010.csv', header=0, encoding='big5')


# adding headers
jan.to_csv('./cleanup/2330/STOCK_DAY_202001.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
feb.to_csv('./cleanup/2330/STOCK_DAY_202002.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
mar.to_csv('./cleanup/2330/STOCK_DAY_202003.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
apr.to_csv('./cleanup/2330/STOCK_DAY_202004.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
may.to_csv('./cleanup/2330/STOCK_DAY_202005.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
jun.to_csv('./cleanup/2330/STOCK_DAY_202006.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
jul.to_csv('./cleanup/2330/STOCK_DAY_202007.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
aug.to_csv('./cleanup/2330/STOCK_DAY_202008.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
sep.to_csv('./cleanup/2330/STOCK_DAY_202009.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
oct.to_csv('./cleanup/2330/STOCK_DAY_202010.csv', header=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])

'''

jan = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202001.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
feb = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202002.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
mar = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202003.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
apr = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202004.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
may = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202005.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
jun = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202006.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
jul = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202007.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
aug = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202008.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
sep = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202009.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])
oct = pd.read_csv('./cleanup/2330/STOCK_DAY_2330_202010.csv', names=["Date", "Shares", "Amount", "Open", "High", "Low", "Close", "Diff", "Turnover"])


'''
print(jan)
print(feb)
print(mar)
print(apr)
print(may)
print(jun)
print(jul)
print(aug)
print(sep)
print(oct)
'''




# concatenate csv files
stock_day_2020 = pd.concat([jan, feb, mar, apr, may, jun, jul, aug, sep, oct], axis=0)

# check
#print('stock_day_2020', stock_day_2020.shape)
#print(stock_day_2020)


'''
#delete unnamed first reference column from concatenation
stock_day_2020 = stock_day_2020.drop(stock_day_2020.columns[0], axis=1)

# miscellaneous
stock_day_2020.to_excel('stockday2020.xlsx', sheet_name='2020', index=False)
stock_day_2020 = pd.read_excel('stockday2020.xlsx', sheet_name='2020')

'''
# output to excel file
stock_day_2020.to_excel('stock_day_2020_clean_1.xlsx', sheet_name='2020', index=False)


