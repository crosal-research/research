######################################################################
# script to draw charts of fiscal policies variables
# initial date: 13/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv("../data/fiscal_policy.csv", header=0, index_col=0)

date_new = "2010-01-01"
df_new = df[df.index >= date_new]

## debt to gdp
trace01 = go.Scatter(x=df_new.index, y=df_new['gross_debt_gdp'],
                     name="Gross Debt to GDP", showlegend=False)
data0 = [trace01]
layout0 = go.Layout(title="<b>Public Sector Gross Debt</b>",
                   yaxis=dict(title="%GDP", tickmode="auto", nticks=5),
                   font=dict(size=18))
fig = go.Figure(data=data0, layout=layout0)
py.image.save_as(fig, "../exhibits/debt_to_gdp_chart.jpeg", format="jpeg")



## flow to gdp
trace11 = go.Scatter(x=df_new.index, y=df_new['primary_gdp'],
                     name="Primary Deficit")
trace12 = go.Scatter(x=df_new.index, y=df_new['interest_gdp'],
                     name="Interest Payments", showlegend=True)
trace13 = go.Scatter(x=df_new.index, y=df_new['total_balance_gdp'],
                     name="Total Balance", showlegend=True)

data1 = [trace11, trace12, trace13]

layout1 = go.Layout(title="<b>Fiscal Policy Stance</b>",
                   yaxis=dict(title="%GDP", tickmode="auto", nticks=5),
                    font=dict(size=18),
                    legend=dict(x=0.0, y=-0.4))
fig = go.Figure(data=data1, layout=layout1)
py.image.save_as(fig, "../exhibits/flow_to_gdp_chart.jpeg", format="jpeg")
