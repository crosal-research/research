######################################################################
# script to draw charts for trade balance
# initial date: 13/07/2016
# todo: add annotation for the last observation
######################################################################

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('../data/trade_balance.csv', index_col=0)
df_12m = df.rolling(window=12).sum()
df_gdp = df_12m.div(df_12m['GDP'], axis=0).iloc[:,:-1]*100

# set date
date_new = "2000-01-01"
df_new = df_gdp[df_gdp.index >= date_new]


## trade balance
trace01 = go.Scatter(x=df_new.index, y=df_new['trade_balance'],
                     name="Trade Balance")
trace02 = go.Scatter(x=df_new.index, y=df_new['good_exports'],
                     name="Exports")
trace03 = go.Scatter(x=df_new.index, y=df_new['good_imports'],
                     name="Imports")
data0 = [trace01, trace02, trace03]
layout0 = go.Layout(title="<b>Trade Balance - 12 months</b>", yaxis=dict(title="%GDP"),
                   font=dict(size=18), legend=dict(x=0, y=-0.4))
fig0 = go.Figure(data=data0, layout=layout0)
py.image.save_as(fig0, '../exhibits/trade_balance_chart.jpeg', format='jpeg')


## trade balance
date_cc = "2000-01-01"
df_cc = df_gdp[df_gdp.index >= date_new]

trace11 = go.Scatter(x=df_new.index, y=df_new['current_account'],
                     name="Current Account")
trace12 = go.Scatter(x=df_new.index, y=df_new['cc_reveneus'],
                     name="Revenues")
trace13 = go.Scatter(x=df_new.index, y=df_new['cc_spending'],
                     name="Spendings")
data1 = [trace11, trace12, trace13]
layout1 = go.Layout(title="<b>Current Account - 12 months</b>", yaxis=dict(title="%GDP"),
                   font=dict(size=18), legend=dict(x=0, y=-0.4))
fig = go.Figure(data=data1, layout=layout1)
py.image.save_as(fig, '../exhibits/current_account_chart.jpeg', format='jpeg')
