######################################################################
# script to draw charts on credit quality
# initial date 14/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/credit_quality.csv", header=0, index_col=0)


## chart on credit quality
trace01 = go.Scatter(x=df.index, y=df['total_del'], name="Total")
trace02 = go.Scatter(x=df.index, y=df['companies_del'], name="Companies")
trace03 = go.Scatter(x=df.index, y=df['households_del'], name="Households")
data0 = [trace01, trace02, trace03]
layout0 = go.Layout(title="<b>Credit Quality</b>",
                    yaxis=dict(title="%Credit by Borrower Typer", tickmode="auto", nticks=5),
                    font=dict(size=18), legend=dict(x=0, y=-0.4))
fig0 = go.Figure(data=data0, layout=layout0)

py.image.save_as(fig0,"../exhibits/credit_quality.jpeg",format="jpeg")


## chart on interest rate
trace11 = go.Scatter(x=df.index, y=df['total_juros'], name="Total")
trace12 = go.Scatter(x=df.index, y=df['companies_juros'], name="Companies")
trace13 = go.Scatter(x=df.index, y=df['households_juros'], name="Households")
data1 = [trace11, trace12, trace13]
layout1 = go.Layout(title="<b>Interest Rates</b>",
                    yaxis=dict(title="%p.y.", tickmode="auto", nticks=5),
                    font=dict(size=18), legend=dict(x=0, y=-0.4))
fig0 = go.Figure(data=data1, layout=layout1)

py.image.save_as(fig0,"../exhibits/credit_interest.jpeg",format="jpeg")
