######################################################################
# script to draw core cpi for Brazil
# initial date: 16/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv("../data/cpi_core_bz.csv", index_col=0).dropna()
df_12m = ((df/100 + 1).cumprod().pct_change(periods=12)*100).dropna()



new_date = "2014-01-01"
df_12m_new = df_12m[df_12m.index >= new_date]

## chart: core
trace01 = go.Scatter(x=df_12m_new.index, y=df_12m_new['cpi'], name="cpi")
trace02 = go.Scatter(x=df_12m_new.index, y=df_12m_new['monitored'], name="monitored")
trace03 = go.Scatter(x=df_12m_new.index, y=df_12m_new['free'], name="free")

data0 = [trace01, trace02, trace03]
layout0 = go.Layout(title="<b>CPI - Core Components</b>",
                    yaxis=dict(title="%yoy", tickmode="auto", nticks=5),
                    font=dict(size=18), legend=dict(x=0, y=-0.4))
fig0 = go.Figure(data=data0, layout=layout0)
py.image.save_as(fig0,"../exhibits/cpi_core_comp.jpeg",format="jpeg")


## chart: free
trace11 = go.Scatter(x=df_12m_new.index, y=df_12m_new['free'], name="free")
trace12 = go.Scatter(x=df_12m_new.index, y=df_12m_new['tradables'], name="tradables")
trace13 = go.Scatter(x=df_12m_new.index, y=df_12m_new['non-tradables'], name="non-tradables")

data1 = [trace11, trace12, trace13]
layout1 = go.Layout(title="<b>CPI Free - Components</b>",
                    yaxis=dict(title="%yoy", tickmode="auto", nticks=5),
                    font=dict(size=18), legend=dict(x=0, y=-0.4))
fig1 = go.Figure(data=data1, layout=layout1)
py.image.save_as(fig1,"../exhibits/cpi_free_comp.jpeg",format="jpeg")
