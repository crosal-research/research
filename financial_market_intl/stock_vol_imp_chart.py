######################################################################
# script to draw implicy volatilities charts
# initial date: 13/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("../data/stock_vol_imp.csv", header=0, index_col=0)



## vixes
date_new = "2014-01-01"
df_new = df[df.index >= date_new]

trace01 = go.Scatter(x=df_new.index, y = df_new['VIXCLS'], name = "VIX")
trace02 = go.Scatter(x=df_new.index, y = df_new['VXEEMCLS'], name = "VOL - EM")
trace03 = go.Scatter(x=df_new.index, y = df_new['VXEWZCLS'], name = "VOL - Brazil")
data = [trace01, trace02, trace03]
layout = go.Layout(title="<b>Implicit Vol - Stock Markets</b>",
                   yaxis=dict(title="pts", tickmode="auto", nticks=5),
                   font=dict(size=18), legend=dict(x=0, y=-0.4))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "../exhibits/stock_vol_imp.jpeg", format="jpeg")
