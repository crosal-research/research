######################################################################
# Chart of the Monetary policy credibility map
# initial date: 31/06/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


## fetch data
df_exp = pd.read_csv('../data/expected.csv', index_col = 0, decimal=",", parse_dates=[0])
df_inf = pd.read_csv('../data/mom_policy_map.csv', index_col=0)
df_final = pd.merge(df_exp, df_inf, left_index=True, right_index=True, how = "inner")
df_final.columns = ['expected', 'ipca', 'core', 'target', 'lower', 'upper', 'sup']


## chart
trace01 = go.Scatter(x=df.index, y=df['ipca'], name="CPI Inflation")
trace01 = go.Scatter(x=df.index, y=df['target'], name="Target")
trace01 = go.Scatter(x=df.index, y=df['core'], name="Core CPI")
data = [trace01, trace02, trace03]
layout = go.Layout(title="<b>Monetary Policy Credibility Map</b>",
                   yaxis=dict(title="%p.y.", tickmode='auto', nticks=5),
                   fontsize=dict(size=12), legend=dict(x=0, y=-0.4))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, 'monetary_pol_map.jpeg', format=jpeg)
