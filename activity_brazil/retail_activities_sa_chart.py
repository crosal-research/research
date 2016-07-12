######################################################################
# script to draw retail sales for Brazil
# initial date: 11/07/2016
######################################################################p
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# fetch data
df = pd.read_csv("../data/retail_activities_sa.csv", index_col=[0])
df_mave = df.rolling(window=3).mean()

### total sales
df_total = pd.merge(pd.DataFrame(df['Total']), pd.DataFrame(df_mave['Total']),
                    left_index=True,  right_index=True,
                    how="inner").pct_change(periods=1) * 100
df_total.columns = ["total", "ma"]

df_total_last = df_total.iloc[-1:, :]
start_date = "2015-10-01"
df_total_new = df_total[df_total.index >= start_date]


# chart
trace01 = go.Scatter(x=df_total_new.index,
                     y = df_total_new['total'], name = "Total")
trace02 = go.Bar(x=df_total_new.index,
                     y = df_total_new['ma'], name = "Moving Average")
trace03 = go.Scatter(x=df_total_last.index, y=df_total_last['total'],
                    mode="markers+text",
                    text=["<b>"+str(round(df_total_last.values[0][0]))+"</b>"],
                     textposition='leftl', showlegend=False)

data = [trace01, trace02, trace03]


layout = go.Layout(title="<b>Retail Sales</b>", legend=dict(x=0, y=-0.4),
                   font=dict(size=18), yaxis=dict(title="%", tickmode="auto", nticks=5))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "../exhibits/retail_total_chart.jpeg", format="jpeg")
