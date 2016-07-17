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
df_mid = pd.merge(df_exp, df_inf, left_index=True, right_index=True, how = "inner")
df_mid.columns = ['expected', 'ipca', 'core', 'target', 'lower', 'upper']


new_date = "2010-01-01"
df_final = df_mid[df_mid.index >= new_date]


## chart
trace01 = go.Scatter(x=df_final.index, y=df_final['ipca'],
                     name="CPI Inflation", line=dict(color="orange"))
trace02 = go.Scatter(x=df_final.index, y=df_final['target'],
                     name="Target", line=dict(color="red"))
trace03 = go.Scatter(x=df_final.index, y=df_final['core'],
                     name="Core CPI")
trace04 = go.Scatter(x=df_final.index, y=df_final['expected'],
                      name="Expeted CPI - One year", line=dict(color="black"))
trace05 = go.Scatter(x=df_final.index, y=df_final['upper'],
                     name="Upper Limit", line=dict(color="red", dash="dot"),
                     showlegend=False)
trace06 = go.Scatter(x=df_final.index, y=df_final['lower'],
                     name="Lower Limit", line=dict(color="red", dash="dot"),
                     showlegend=False)
data = [trace01, trace02, trace03, trace04, trace05, trace06]
layout = go.Layout(title="<b>Monetary Policy Credibility Map</b>",
                   yaxis=dict(title="%mom", tickmode='auto', nticks=5),
                   font=dict(size=18), legend=dict(x=0, y=-0.6))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, '../exhibits/monetary_pol_map.jpeg', format="jpeg")
