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
trace01 = go.Scatter(x=df_final.index, y=df_final['ipca'],
                     name="CPI Inflation")
trace02 = go.Scatter(x=df_final.index, y=df_final['target'],
                     name="Target")
trace03 = go.Scatter(x=df_final.index, y=df_final['core'],
                     name="Core CPI")
trace04 = go.Scatter(x=df_final.index, y=df_final['expected'],
                      name="Expeted CPI - One year")
trace05 = go.Scatter(x=df_final.index, y=df_final['upper'],
                     name="Upper Limit", line=dict(color="red", dash="dot"))
trace06 = go.Scatter(x=df_final.index, y=df_final['lower'],
                     name="Lower Limit", line=dict(color="red", dash="dot"))
data = [trace01, trace02, trace03, trace04, trace05, trace06]
layout = go.Layout(title="<b>Monetary Policy Credibility Map</b>",
                   yaxis=dict(title="%p.y.", tickmode='auto', nticks=5),
                   font=dict(size=12), legend=dict(x=0, y=-0.4))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, 'monetary_pol_map.jpeg', format="jpeg")
