#! /usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('./raw-data/20201213/owid-covid-data.csv')

print(df.info())
print(df['continent'].unique())

asia = df.loc[(df.continent == 'Asia') & (df.new_cases > 5000)]
europe = df.loc[(df.continent == 'Europe') & (df.new_cases > 10000)]
africa = df.loc[(df.continent == 'Africa') & (df.new_cases > 1000)]
na = df.loc[(df.continent == 'North America') & (df.new_cases > 10000)]
sa = df.loc[(df.continent == 'South America') & (df.new_cases > 10000)]
oceania = df.loc[(df.continent == 'Oceania') & (df.new_cases > 10)]


## fit all graphs in one figures. trouble showing all datasets.
# =======================================================================
# fig,((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
#
# ax1.scatter(asia['date'].sort_values(), asia['new_cases'], marker='.')
# ax1.set_title('Asia')
# ax1.xaxis.set_major_locator(ticker.MultipleLocator(20))
# ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
# ax2.scatter(europe['date'].sort_values(), europe['new_cases'], marker='.')
# ax2.set_title('Europe')
# ax2.xaxis.set_major_locator(ticker.MultipleLocator(10))
# ax2.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
# ax3.scatter(africa['date'].sort_values(), africa['new_cases'], marker='.')
# ax3.set_title('Africa')
# ax3.xaxis.set_major_locator(ticker.MultipleLocator(20))
# ax3.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
# ax4.scatter(na['date'].sort_values(), na['new_cases'], marker='.')
# ax4.set_title('North America')
# ax4.xaxis.set_major_locator(ticker.MultipleLocator(30))
# ax4.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
# ax5.scatter(sa['date'].sort_values(), sa['new_cases'], marker='.')
# ax5.set_title('South America')
# ax5.xaxis.set_major_locator(ticker.MultipleLocator(20))
# ax5.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
# ax6.set_title('Oceania')
# ax6.xaxis.set_major_locator(ticker.MultipleLocator(10))
# ax6.xaxis.set_minor_locator(ticker.MultipleLocator(1))
#
# fig.suptitle('New Cases', fontsize=16)
# fig.tight_layout()
# fig.autofmt_xdate()
# plt.savefig('all-test.png', dpi=3000)
# =======================================================================

# Saving data for each continent
# =======================================================================
fig1, ax1 = plt.subplots(1)
ax1.scatter(asia['date'].sort_values(), asia['new_cases'], marker='.')
ax1.set_title('Asia')
ax1.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
fig1.suptitle('New Cases', fontsize=16)
fig1.tight_layout()
fig1.autofmt_xdate()
plt.savefig('cont-asia.png', dpi=1000)

fig2, ax2 = plt.subplots(1)
ax2.scatter(europe['date'].sort_values(), europe['new_cases'], marker='.')
ax2.set_title('Europe')
ax2.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax2.xaxis.set_minor_locator(ticker.MultipleLocator(1))
fig2.suptitle('New Cases', fontsize=16)
fig2.tight_layout()
fig2.autofmt_xdate()
plt.savefig('cont-europe.png', dpi=1000)

fig3, ax3 = plt.subplots(1)
ax3.scatter(africa['date'].sort_values(), africa['new_cases'], marker='.')
ax3.set_title('Africa')
ax3.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax3.xaxis.set_minor_locator(ticker.MultipleLocator(1))
fig3.suptitle('New Cases', fontsize=16)
fig3.tight_layout()
fig3.autofmt_xdate()
plt.savefig('cont-africa.png', dpi=1000)

fig4, ax4 = plt.subplots(1)
ax4.scatter(na['date'].sort_values(), na['new_cases'], marker='.')
ax4.set_title('North America')
ax4.xaxis.set_major_locator(ticker.MultipleLocator(30))
ax4.xaxis.set_minor_locator(ticker.MultipleLocator(1))
fig4.suptitle('New Cases', fontsize=16)
fig4.tight_layout()
fig4.autofmt_xdate()
plt.savefig('cont-na.png', dpi=1000)

fig5, ax5 = plt.subplots(1)
ax5.scatter(sa['date'].sort_values(), sa['new_cases'], marker='.')
ax5.set_title('South America')
ax5.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax5.xaxis.set_minor_locator(ticker.MultipleLocator(1))
fig5.suptitle('New Cases', fontsize=16)
fig5.tight_layout()
fig5.autofmt_xdate()
plt.savefig('cont-sa.png', dpi=1000)

fig6, ax6 = plt.subplots(1)
ax6.scatter(oceania['date'].sort_values(), oceania['new_cases'], marker='.')
ax6.set_title('Oceania')
ax6.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax6.xaxis.set_minor_locator(ticker.MultipleLocator(1))
fig6.suptitle('New Cases', fontsize=16)
fig6.tight_layout()
fig6.autofmt_xdate()
plt.savefig('cont-oceania.png', dpi=1000)
# =======================================================================
