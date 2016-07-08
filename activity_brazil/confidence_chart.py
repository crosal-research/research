######################################################################
# script to draw (sub) plots of service and consumer confidence Brazil
# data: 16/06/2016
######################################################################

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('../data/confianca.csv', index_col=0, header=0,
                 names = ["service", "consumer"])

start_date = "2008-06-01"
df_new = df[df.index >= start_date]

# chart: confidence - service
trace0 = go.Scatter(x=df_new.index, y=df_new['service'])
data = [trace0]
layout = go.Layout(title="<b>Service Sector Confidence Index</b>",
                   font=dict(size=24))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "../exhibits/confidence_service.jpeg")


start_date = "2008-06-01"
df_new = df[df.index >= start_date]

# chart: confidence - consumer
trace0 = go.Scatter(x=df_new.index, y=df_new['consumer'])
data = [trace0]
layout = go.Layout(title="<b>Consumer Confidence Index</b>",
                   font=dict(size=24))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "../exhibits/confidence_consumer.jpeg")
