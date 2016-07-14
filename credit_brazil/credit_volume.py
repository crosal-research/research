######################################################################
# script to draw charts for Brazil's credit volume
# initial date: 14/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('../data/credit_volume.csv', index_col=0)
df_ch = df.pct_change(periods=12)*100
df_12m = df.rolling(window=12).sum().dropna()
df_gdp = df_12m.div(df_12m['GDP'], axis=0).iloc[:,1:]*10

new_date = "2010-01-01"
df_gdp_new = df_gdp[df_gdp.index >= new_date]

## volume
trace01 = go.Scatter(x=df_gdp_new.index, y=df_gdp_new['Total'], name="Total")
trace02 = go.Scatter(x=df_gdp_new.index, y=df_gdp_new['Institutions'], name="Institutions")
trace03 = go.Scatter(x=df_gdp_new.index, y=df_gdp_new['Households'], name="Households")
data0 = [trace01, trace02, trace03]
layout0 = go.Layout(title="<b>Credit Volume</b>",
                    yaxis=dict(title="%GDP", tickmode="auto", nticks=5),
                    font=dict(size=18),
                    legend=dict(x=0, y=-0.4))
fig = go.Figure(data=data0, layout=layout0)
py.image.save_as(fig, '../exhibits/credit_gdp_chart.jpeg', format="jpeg")
