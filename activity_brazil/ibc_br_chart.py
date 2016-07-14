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
def month_ma_chart(date_new, df_ma, name1, name2, title):
    df_new = df_ma[df_ma.index >= date_new]
    trace01 = go.Scatter(x=df_new.index, y=df_new.iloc[:,0], name=name1)
    trace02 = go.Bar(x=df_new.index, y=df_new.iloc[:,1], name=name2)
    data0 = [trace01, trace02]
    layout0 = go.Layout(title="<b>{}</b>".format(title),
                        yaxis=dict(title="%momsa", tickmode="auto", nticks=5),
                        font=dict(size=18), legend=dict(x=0, y=-0.4))
    return go.Figure(data=data0, layout=layout0)

py.image.save_as(month_ma_chart("2015-02-01",
                           df_ma, "IBC-br", "3M ma", "IBC-br"),
                 "../exhibits/ibc_br_chart.jpeg",format="jpeg")
