######################################################################
# script to draw chart on several currencies
# initial date: 10/10/2016
#####################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("../data/currencies.csv", index_col=[0])


brexit = "2016-06-22"

def chart_gen(df, leg, date_ini): #, title, y_title, leng, date_ini):
    df_final = df[df.index >= date_ini] / df[df.index==date_ini].iloc[0]
    data = []
    for i in range(len(df.columns)):
        dat = go.Scatter(x=df_final.index, y=df_final.iloc[:,i], name=leg[i])
        data.append(dat)
    layout = go.Layout(title="whatever")
    return go.Figure(data=data, layout=layout)

py.image.save_as(chart_gen(df, df.columns, brexit), "../exhibits/currencies.jpeg",
                 format="jpeg")
