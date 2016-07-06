######################################################################
# script to draw plot with import versus exports trade flow (quantum)
# data: 06/07/2016
######################################################################

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('../data/trade_flow_quantum.csv', index_col=0, header=0,
                 names = ["import", "export"])



start_date = "2009-01-01"
df_final = df[df.index >= start_date]

# chart: Volume
trace0 = go.Scatter(x=df_final.index, y=df_final['import'], name="Import",
                    line=dict(color="red"))
trace1 = go.Scatter(x=df_final.index, y=df_final['export'], name="Export",
                    line=dict(color='export'))
data = [trace0, trace1]
layout = go.Layout(title="<b>Trade Flow (Volume)</b>",
                   font=dict(size=24),
                   yaxis=dict(title="Pts (2006=100)", tickmode="auto",
                              nticks="5"))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "../exhibits/trade_flow_quantum.jpeg", format="jpeg")
