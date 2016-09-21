######################################################################
# script to draw chart of shiller's cape
# last version: 16/06/2016
######################################################################

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('../data/shiller_ave.csv', index_col=0, header=0)
df.columns = ["Cape", "Average"]

# chart
def gen_chart(df, title, y_title, date_ini, source=True):
    '''
    Produces plot.ly figure from a dataframe, the title, y title,
    initial date and add crosal label.
    inputs:
    ------
    - df: Dataframe
    - tittle: str
    - y_title: str
    - date_ni: str (ex: Y%-%m-%d)
    -source: boolean
    Outputs:
    -------
    - plot.ly figure
    '''
    df_final = df[df.index >= date_ini]
    data = []
    # Choose colors from http://colorbrewer2.org/ under "Export"
    color = np.array(['rgb(166,206,227)','rgb(31,120,180)','rgb(178,223,138)',
             'rgb(51,160,44)','rgb(251,154,153)','rgb(227,26,28)',
             'rgb(253,191,111)','rgb(255,127,0)','rgb(202,178,214)',
             'rgb(106,61,154)','rgb(255,255,153)','rgb(177,89,40)'])
    for c in df_final.columns:
        if c == "Average":
            data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).loc[:, c],
                                   marker=dict(color=color[df.columns == c][0]),
                                   showlegend=False, mode="markers + text",
                                   text=["<b>"+str(round(df_final.tail(1).loc[:, c].values[0], 1))+"</b>"],
                                   textposition='top left',
                                   textfont=dict(size=16)))
            dat = go.Scatter(x=df_final.index, y=df_final.loc[:, c],
                             name=c, marker=dict(color = color[df.columns == c][0]),
                             mode="lines", line=dict(dash="dash"))
            data.append(dat)
        else:
            data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).loc[:, c],
                                   marker=dict(color=color[df.columns == c][0]),
                                   showlegend=False, mode="markers+text",
                                   text=["<b>"+str(round(df_final.tail(1).loc[:, c].values[0], 1))+"</b>"],
                                   textposition='top left',
                                   textfont=dict(size=16)))
            dat = go.Scatter(x=df_final.index, y=df_final.loc[:, c],
                             name=c, marker=dict(color = color[df.columns == c][0]))
            data.append(dat)

    layout = go.Layout(title="<b>{}</b>".format(title),
                       font=dict(size=22),
                       yaxis=dict(title=y_title, tickmode="auto", nticks=5),
                       legend=dict(x=0, y=-0.4),
                       annotations=[dict(x=df_final.tail(1).index.values[0],
                                         y=df_final.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df_final.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=16)),
                                    dict(
                                        x=.95,
                                        y= -0.4,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=16, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        opacity=0.5,
                                        showarrow=False
                                    )])

    return go.Figure(data=data, layout=layout)


date_init = "1950-01-01"
fig = gen_chart(df, "S&P's Cyclically Adjusted PE", "Earnings", date_init)
py.image.save_as(fig, '../exhibits/shiller.jpeg', format="jpeg")
