######################################################################
# script to draw financial stability rations form brazil
# initial date: 15/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/financial_stability_bz.csv", index_col=0)

new_date = "2010-01-01"
df_new = df[df.index >= new_date]

## Capital Ratios
trace01 = go.Scatter(x=df_new.index, y = df_new['basel_index'],
                     name="Basel Index (over risk adjusted Assets)")
trace02 = go.Scatter(x=df_new.index, y = df_new['leverage_ratio'], name="Leverage Ratio")
data0 = [trace01, trace02]
layout0 = go.Layout(title="<b>Capital Ratios</b>",
                    yaxis=dict(title="%Assets", tickmode="auto", nticks=5),
                    font=dict(size=18), legend=dict(x=0, y=-0.4))

fig0 = go.Figure(data=data0, layout=layout0)
py.image.save_as(fig0,"../exhibits/capital_ratio_bz.jpeg",format="jpeg")
