######################################################################
# script to draw chart on several currencies
# initial date: 10/10/2016
#####################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("../data/currencies.csv", index_col=[0])
curs = [u'Australian Dollar', u'Brazilian Real', u'Indian Ruppee',
        u'Russian Ruble', u'Turkish Lira', u'Canadian Dollar',
        u'New Zealand Dollar', u'South African Rand']
df_curs = df.loc[:, curs]

brexit = "2016-06-22"

def chart_gen(df, leg, date_ini): #, title, y_title, leng, date_ini):
    df_final = (df[df.index >= date_ini] / df[df.index==date_ini].iloc[0] -1)*100
    data = []
    for i in range(len(df.columns)):
        if leg[i] == 'Brazilian Real':
            dat = go.Scatter(x=df_final.index, y=df_final.iloc[:,i], name=leg[i],
                             line=dict(width=4))
            data.append(dat)
        else:
            dat = go.Scatter(x=df_final.index, y=df_final.iloc[:,i], name=leg[i])
            data.append(dat)
    layout = go.Layout(title="<b>Commodity Producers and EM Currencies </b> </br> (since Brexit)",
                       font=dict(size=18),
                       yaxis=dict(tickmode='auto', nticks=5, tickfont=dict(size=14)),
                       xaxis=dict(tickfont=dict(size=14)),
                       legend=dict(y=0.3, font=dict(size=14)))
    return go.Figure(data=data, layout=layout)

py.image.save_as(chart_gen(df_curs, df_curs.columns, brexit), "../exhibits/currencies.jpeg",
                 format="jpeg")
