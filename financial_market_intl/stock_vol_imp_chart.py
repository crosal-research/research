######################################################################
# script to draw implicy volatilities charts
# initial date: 13/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("../data/stock_vol_imp.csv", header=0, index_col=0, na_values = ["."])

## vixes
date_new = "2015-01-01"
df_new = df[df.index >= date_new].dropna()

trace01 = go.Scatter(x=df_new.index, y = df_new['VIXCLS'], name = "VIX")
trace02 = go.Scatter(x=df_new.index, y = df_new['VXEEMCLS'], name = "VOL - EM")
trace03 = go.Scatter(x=df_new.index, y = df_new['VXEWZCLS'], name = "VOL - Brazil")
data = [trace01, trace02, trace03]
layout = go.Layout(title="<b>Implicit Vol - Stock Markets</b>",
                   yaxis=dict(title="pts", tickmode="auto", nticks=5),
                   font=dict(size=18), legend=dict(x=0, y=-0.4))

brexit = "2016-06-23"
layout.update(dict(
    shapes=[
        {"type": 'line',
         'xref': 'x',
         'yref': 'y',
         'x0': brexit,
         'y0': 0,
         'x1': brexit,
         'y1': df_new['VXEWZCLS'].max()+5,
         'line': dict(dash="dot", color="blue")
        }],
    annotations=[go.Annotation(text="Brexit", x=brexit,
                               y=df_new["VXEWZCLS"].max())]))

fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "../exhibits/stock_vol_imp.jpeg", format="jpeg")


## vix

ave_vix = df["VIXCLS"].mean()
df_vix = pd.merge(pd.DataFrame(np.ones(df.shape[0])*ave_vix, index = df.index),
                  pd.DataFrame(df["VIXCLS"].values,index=df.index),
                  right_index=True, left_index=True, how="inner")
df_vix.columns = ["mean", "vix"]

date_vix = "2014-01-01"
df_vix_new = df_vix[df_vix.index >= date_vix]

trace11 = go.Scatter(x=df_vix_new.index, y = df_vix_new['vix'], name = "VIX")
trace12 = go.Scatter(x=df_vix_new.index, y = df_vix_new['mean'], name = "Average",
                     line=dict(dash="dash"))
data1 = [trace11, trace12]
layout1 = go.Layout(title="<b>VIX</b>",
                   yaxis=dict(title="pts", tickmode="auto", nticks=5),
                   font=dict(size=18), legend=dict(x=0, y=-0.4))
fig = go.Figure(data=data1, layout=layout1)
py.image.save_as(fig, "../exhibits/vix_chart.jpeg", format="jpeg")
