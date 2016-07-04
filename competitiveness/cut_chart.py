######################################################################
# draw chart for unit labor cost
# initial date: 04/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('../data/cut.csv', index_col=0)
n = [1.0 for i in range(0, df.size)]
df_ave = pd.DataFrame(n, index=df.index, columns = ['average']) * df.mean()[0]
df_mid = pd.merge(df, df_ave, left_index=True, right_index=True, how="inner")


start_date = '1995-01-01'
df_final = df_mid[df_mid.index >= start_date]

## chart
trace01 = go.Scatter(x=df_final.index, y=df_final['cut'], name = "Unit Labor Cost")
trace02 = go.Scatter(x=df_final.index, y=df_final['average'], name = "Average",
                     line=dict(color="red", dash="dot"))
data = [trace01, trace02]
layout = go.Layout(title="<b>Unit Labor Cost - Brazil </b>",
                   font=dict(size=12), legend=dict(x=0, y = -0.2),
                   yaxis=dict(title="pts", tickmode="auto", nticks=5))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, 'cut.jpeg', format="jpeg")
