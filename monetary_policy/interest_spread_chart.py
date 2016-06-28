######################################################################
# Chart for interest rates sprads
# initial date: 28/06/2016
######################################################################

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/interest_spread.csv", header=0, index_col=0)
df.columns = ["selic", "cdi6m", 'cdi1y']

start_data = "2016-05-01"
df_cut = df[df.index >= start_data]

## chart
trace01 = go.Scatter(x=df_cut.index, y=df_cut['selic'])
trace02 = go.Scatter(x=df_cut.index, y=df_cut['cdi6m'])
trace03 = go.Scatter(x=df_cut.index, y=df_cut['cdi1y'])

data = [trace01, trace02, trace03]
layout = go.Layout(title = "<b>Interest Rates Term Premium</b>")
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, 'interest_spreads.jpeg', format="jpeg")
