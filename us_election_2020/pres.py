#! /usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

pres_state = pd.read_csv('./raw/president_state.csv')

# remove entry of vote sum
f_pres_state = pres_state.drop(pres_state.loc[pres_state['state']=='United States'].index)

# divide votes by million
f_pres_state['total_v_mil'] = f_pres_state['total_votes'].div(1000000)

# find states with more than 1m votes
o1m = f_pres_state.loc[(f_pres_state['total_v_mil'] > 1)]


# plots
fig, ax = plt.subplots()
ax.bar(o1m['state'],o1m['total_v_mil'])
ax.set_title('States')
ax.set_ylabel('million')
#ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
fig.suptitle('Total Votes', fontsize=16)
fig.tight_layout()
fig.autofmt_xdate()
plt.show()



