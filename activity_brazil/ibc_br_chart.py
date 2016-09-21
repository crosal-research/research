######################################################################
# script to draw charts on IBC-br
# initial date 14/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/ibc_br.csv", header=0, index_col=0)
df_ma = pd.merge(pd.DataFrame(df['ibc_br_sa']),
                 pd.DataFrame(df['ibc_br_sa'].rolling(window=3).mean()),
                 left_index=True, right_index=True,
                 how="inner").pct_change(periods=1)*100
df_ma.columns = ["ibc_sa", "ibc_ma"]



## chart on ibc_br
def month_ma_chart(date_new, df_ma, name1, name2, title, source=True):
    df_new = df_ma[df_ma.index >= date_new]
    trace01 = go.Scatter(x=df_new.index, y=df_new.iloc[:,0], name=name1)
    trace02 = go.Bar(x=df_new.index, y=df_new.iloc[:,1], name=name2)
    trace03 = go.Scatter(x=df_new.tail(1).index, y=df_new.tail(1).iloc[:,0],
                         mode="markers+text",
                         text=["<b>"+str(round(df_new.tail(1).iloc[:,0].values[0],2))+"</b>"],
                         textposition='left', showlegend=False)
    data0 = [trace01, trace02, trace03]
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title="%momsa", tickmode="auto", nticks=5, range=[-1.5, 1.5]),
                       xaxis = dict(tickangle=0, tickmode="auto", nticks=4),
                       font=dict(size=22), legend=dict(x=0, y=-0.4),
                       annotations=[dict(x=df_new.tail(1).index.values[0],
                                         y=df.max().max()-5,
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df_new.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=16)),
                                    dict(x=.95,
                                        y= -0.4,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=16, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        opacity=0.5,
                                         showarrow=False)])

    return go.Figure(data=data0, layout=layout)

py.image.save_as(month_ma_chart("2015-02-01",
                                df_ma, "%momsa", "3Mma %momsa", "GDP Monthly Tracker (IBC-br)"),
                 "../exhibits/ibc_br_chart.jpeg",format="jpeg")
