######################################################################
# script to draw chart on terms of trade, brazil
# initial date: 15/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py_
import plotly.graph_objs as go

df = pd.read_csv("../data/terms_of_trade.csv", index_col=[0])
df_tt = df.iloc[:,1] / df.iloc[:,0]
dn = ((df_tt - df_tt.mean())/df_tt.mean())*100

##
def gen_chart(df, title, y_title, leg, date_ini):
    df_final = df[df.index >= date_ini]
    trace01 = go.Scatter(x=df_final.index, y=df_final,
                         name=leg, showlegend=False)
    trace02 = go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1),
                             mode="markers+text",
                             text=["<b>"+str(round(df_final.tail(1).values[0], 1))+"</b>"],
                             textposition='top', showlegend=False)
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title="".format(y_title),
                                  tickmode="auto", nticks=5),
                       font=dict(size=18))
    return go.Figure(data=[trace01, trace02], layout=layout)


py.image.save_as(gen_chart(dn, "Terms of Trade - Brazil",
                           "%Deviations from Mean", "terms of trade",
                           "2000-01-01"), "../exhibits/terms_of_trade.jpeg",
                 format="jpeg")
