######################################################################
# script to draw chart for terms of trade
# initial date: 04/07/2016
######################################################################
import pandas as pd
import os
import plotly.plotly as py
import plotly.graph_objs as go

caminho="/home/jmrosal/Documents/crosal/research/research/exhibits/"


## fetch data and transform
df = pd.read_csv('../data/terms_of_trade.csv', index_col=0)
df_mid = pd.DataFrame(df['export'].div(df['import'], axis=0), columns=["terms"])
df_new = (df_mid.div(df_mid.mean(),axis=1)-1)*100


def gen_chart(df, title, y_title, date_ini, source=True):
    df_final = df_new[df_new.index >= date_ini]
    data = [go.Scatter(x=df_final.index, y=df_final['terms'],
                         name = "Terms of Trade")]
    layout = go.Layout(title="<b>{}</b>".format(title),
                       font=dict(size=22),
                       yaxis=dict(title="% (average=0)", tickmode="auto", nticks="5"),
                       legend=dict(x=0, y=-0.2),
                       showlegend=False,
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=16)),
                                    dict(
                                        x=.95,
                                        y= -0.2,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=16, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        opacity=0.5,
                                        showarrow=False
                                    )])

    return go.Figure(data=data, layout=layout)


date_ini = "1995-01-01"
py.image.save_as(gen_chart(df_new, "Term of Trade", "%", date_ini),
                 os.path.join(caminho, "terms_of_trade.jpeg"), format="jpeg")
