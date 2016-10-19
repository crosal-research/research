######################################################################
# Chart for interest rates sprads
# initial date: 28/06/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("../data/interest_spread.csv", header=0, index_col=0,
                 usecols=[0, 1,4,5]).fillna(method='ffill')
df.columns = ["Selic", "6M Interbank", "1Y interbank"]

## chart
def chart_gen(df, title, y_title, data_ini, last_meeting):
    df_cut = df[start_date:]
    color = np.array(['rgb(166,206,227)','rgb(31,120,180)','rgb(178,223,138)',
                      'rgb(51,160,44)','rgb(251,154,153)','rgb(227,26,28)',
                      'rgb(253,191,111)','rgb(255,127,0)','rgb(202,178,214)',
                      'rgb(106,61,154)','rgb(255,255,153)','rgb(177,89,40)'])
    data = []
    for c in df.columns:
        trace = go.Scatter(x=df_cut.index, y=df_cut.loc[:,c], name=c,
                           marker=dict(color=color[df.columns == c[0]]))
        data.append(go.Scatter(x=df_cut.tail(1).index, y=df_cut.tail(1).loc[:, c],
                               marker=dict(color=color[df.columns == c][0]),
                               showlegend=False, mode="markers+text",
                               text=["<b>"+str(round(df_cut.tail(1).loc[:, c].values[0], 1))+"</b>"],
                               textposition='top left',
                               textfont=dict(size=16)))
        data.append(trace)
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title="{}".format(y_title), tickmode="auto", nticks=5),
                       font=dict(size=18), legend=dict(x=0, y=-0.4),
                       annotations=[dict(x=df_cut.tail(1).index.values[0],
                                         y=df_cut.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df_cut.tail(1).index).strftime("%b-%d-%Y")[0]+"</b>",
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
                                    ),
                                    dict(x=last_meeting,
                                         y =15.5,
                                         text="Last COPOM")],
                       shapes=[
                           dict(
                               type = 'line',
                               x0 = last_meeting,
                               y0 = 13,
                               x1 = last_meeting,
                               y1 = 15,
                               line = dict(
                                   color='black',
                                   width= 3,
                                   dash='dot'
                                   )
                               )
                           ])

    return go.Figure(data=data, layout=layout)


#generate chart
start_date = "2016-04-01"
last_meeting = '2016-08-31'
py.image.save_as(chart_gen(df, "Interest Rate Term Structure",
                           "%p.y.", start_date, last_meeting),
                 '../exhibits/interest_spreads.jpeg', format="jpeg")
