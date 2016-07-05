######################################################################
# script to draw chart of shiller's cape
# last version: 16/06/2016
######################################################################

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/shiller_ave.csv', index_col=0, header=0)

# chart
trade0 = go.Scatter(x=df.index, y=df['cape'], name = "CAPE",
                    line=dict(width=2))
trade1 = go.Scatter(x=df.index, y=df['ave'], name= "Historical Average",
                    line=dict(width=2, dash="dash"))
data=[trade0, trade1]
layout = go.Layout(title="<b>S&P's Cyclically Adjusted PE <br> (CAPE)</b>",
                   yaxis=dict(title='Earnings  (times)', tickmode="auto", nticks=5),
                   font=dict(size=24),
                   legend=dict(x=0, y=-0.2))


fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, '../exhibits/shiller.jpeg', format="jpeg")
