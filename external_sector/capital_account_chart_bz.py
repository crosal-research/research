######################################################################
# draw data on capital account data
# initial date: 21/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv("../data/net_capital_flow.csv", index_col=0)


## chart
def net_flow(newdate, series, title, ytitle):
    df_new = df[df.index >= newdate]
    df_sum = df.rolling(window=12).mean()
    df_sum_new = df_sum[df_sum.index >= newdate]
    trace01 = go.Scatter(x=df_new.index, y=df_new[series[0]],
                         name="Monthly")
    trace02 = go.Scatter(x=df_sum_new.index, y=df_sum_new[series[0]],
                         name="12M rolling average", line=dict(dash="dot"))
    data0 = [trace01, trace02]
    layout0 = go.Layout(title="<b>{}</b>".format(title),
                        yaxis=dict(title=ytitle, tickmode="auto", nticks=5),
                        font=dict(size=18), legend=dict(x=0, y=-0.4))
    return go.Figure(data=data0, layout=layout0)

py.image.save_as(net_flow("2010-01-01", ["net_financial_account"], "Net Financial Account",
                          ytitle="USDmn"),
                "../exhibits/net_capital_flow.jpeg",format="jpeg")
