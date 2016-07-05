######################################################################
# draw chart for real fx rate
# initial date: 04/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv('../data/real_fx_rate.csv', index_col=0).dropna()
df_mid = (df.div(df.mean(), axis=1)-1)*100


start_date = '1995-01-01'
df_final = df_mid[df_mid.index >= start_date]

## chart
trace01 = go.Scatter(x=df_final.index, y=df_final['fx_real'], name = "Real Effective Fx Rate")
trace02 = go.Scatter(x=df_final.index, y=df_final['fx_prod'], name = "Effective Unit Labor Cost")

data = [trace01, trace02]
layout = go.Layout(title="<b>Effective Exchange Rates</b>",
                   font=dict(size=12), legend=dict(x=0, y = -0.2),
                   yaxis=dict(title="% (0=Average)", tickmode="auto", nticks=5))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, 'real_exchange_rate.jpeg', format="jpeg")
