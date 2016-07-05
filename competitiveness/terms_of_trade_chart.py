######################################################################
# script to draw chart for terms of trade
# initial date: 04/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


## fetch data and transform
df = pd.read_csv('../data/terms_of_trade.csv', index_col=0)
df_mid = pd.DataFrame(df['export'].div(df['import'], axis=0), columns=["terms"])
df_ave = pd.DataFrame([1 for i in range(0, df_mid.size)])*df_mid.mean()[0]
df_ave.set_index(df.index, inplace=True)
df_ave.columns = ['average']
df_new = pd.merge(df_mid, df_ave, left_index=True, right_index=True, how='inner')


start_date = "1995-01-01"
df_final = df_new[df_new.index >= start_date]

## chart
trace01 = go.Scatter(x=df.index, y=df_final['terms'],
                     name = "Terms of Trade")
trace02 = go.Scatter(x=df.index, y=df_final['average'],
                     name = "Average", line=dict(dash='dot', color='red'))
data = [trace01, trace02]
layout = go.Layout(title="<b>Terms of Trade</b>",
                   font=dict(size=12),
                   yaxis=dict(title="pts", tickmode="auto", nticks="5"),
                   legend=dict(x=0, y=-0.2))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "terms_of_trade.jpeg", format="jpeg")
