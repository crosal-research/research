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



def chart_gen(df, leg, date_ini, source=True):

    df_final = (df[df.index >=date_ini] / df[df.index==date_ini].iloc[0] -1)*100
    data = []
    for i in range(len(df.columns)):
        if leg[i] == 'Brazilian Real':
            dat = go.Scatter(x=df_final.index, y=df_final.iloc[:,i], name=leg[i],
                             line=dict(width=3))
            data.append(dat)
        else:
            dat = go.Scatter(x=df_final.index, y=df_final.iloc[:,i], name=leg[i])
            data.append(dat)
    layout = go.Layout(title="<b>Commodity Producers and EMs Currencies</b>",
                       font=dict(size=18),
                       yaxis=dict(tickmode='auto', nticks=5, tickfont=dict(size=14)),
                       xaxis=dict(tickfont=dict(size=14)),
                       legend=dict(y=0.3, font=dict(size=14)),
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14))])

    if source:
        layout.update(dict(annotations=[dict(
            x=.95,
            y=-0.2,
            xref='paper',
            yref='paper',
            text="<b><i>CRosal Independent Research</i></b>",
            font=dict(size=14, family='Courier new', color="#ffffff"),
            bgcolor='#ff8080',
            opacity=0.5,
            showarrow=False
        )]))



    return go.Figure(data=data, layout=layout)


brexit = "2016-08-01"
py.image.save_as(chart_gen(df_curs, df_curs.columns, brexit), "../exhibits/currencies.jpeg",
                 format="jpeg")
