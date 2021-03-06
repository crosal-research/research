######################################################################
# script to draw retail sales for Brazil
# initial date: 11/07/2016
######################################################################

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# fetch data
df = pd.read_csv("../data/ind_atividades_sa.csv", index_col=[0],
                 na_values="-")
df_mave = df.rolling(window=3).mean()

# data manipulation
df_total = pd.merge(pd.DataFrame(df['Geral']), pd.DataFrame(df_mave['Geral']),
                    left_index=True,  right_index=True,
                    how="inner").pct_change(periods=1) * 100
df_total.columns = ["total", "ma"]

# chart

def chart_gen(df, title, leg, y_title, date_ini, source=True):
    df_total_last = df.iloc[-1:, :]
    df_total_new = df[df.index >= date_ini]
    trace01 = go.Scatter(x=df_total_new.index,
                         y=df_total_new.iloc[:,0], name=leg[0])
    trace02 = go.Bar(x=df_total_new.index,
                     y=df_total_new.iloc[:,1], name=leg[1])
    trace03 = go.Scatter(x=df_total_last.index, y=df_total_last.iloc[:, 0],
                         mode="markers+text",
                         text=["<b>"+str(round(df_total_last.values[0][0], 1))+"</b>"],
                         textposition='left', showlegend=False, textfont=dict(size=16))
    data = [trace01, trace02, trace03]
    layout = go.Layout(title="<b>{}</b>".format(title), legend=dict(x=0, y=-0.4),
                       font=dict(size=22), yaxis=dict(title="{}".format(y_title),
                                                      tickmode="auto", nticks=5),
                       annotations=[dict(x=df_total_new.tail(1).index.values[0],
                                         y=df.max().max()-5,
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df_total_new.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=16)),
                                    dict( x=.95,
                                          y= -0.4,
                                          xref='paper',
                                          yref='paper',
                                          text="<b><i>CRosal Independent Research</i></b>",
                                          font=dict(size=16, family='Courier new', color="#ffffff"),
                                          bgcolor='#ff8080',
                                          opacity=0.5,
                                          showarrow=False)])
    return go.Figure(data=data, layout=layout)


# generates chart
start_date = "2015-10-01"
py.image.save_as(chart_gen(df_total, "Industrial Production", ["IP", "ma"],
                           "%mam", start_date),
                "../exhibits/industry_total_chart.jpeg",
                 format="jpeg")
