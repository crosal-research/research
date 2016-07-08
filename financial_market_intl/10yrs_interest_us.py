######################################################################
# script to draw chart of 10 years us treasury
# initial data: 08/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('../data/interest_rates_us.csv', index_col=[0],
                 usecols=[0,1], na_values=["NaN", "."]).dropna()

start_date = "2005-01-01"
df_final = df[df.index >= start_date]


## chart
trace01 = go.Scatter(x=df_final.index, y=df_final['DGS10'])
data = [trace01]
layout = go.Layout(title="<b>Ten Years Treasury</b>", font=dict(size=18),
                   yaxis=dict(title="% p.y", tickmode="auto", nticks=5))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "../exhibits/10yrs_interest_us.jpeg", format="jpeg")
