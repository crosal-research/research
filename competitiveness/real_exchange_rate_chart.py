######################################################################
# draw chart for real fx rate
# initial date: 04/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import os


caminho="/home/jmrosal/Documents/crosal/research/research/exhibits/"

df = pd.read_csv('../data/real_fx_rate.csv', index_col=0).dropna()
df_mid = (df.div(df.mean(), axis=1)-1)*100
df_mid.columns = ["Real Effective Fx Rate", "Real Unit Labor Cost"]


## chart
def gen_chart(df, title, y_title, date_ini, source=True):
    df_final = df[df.index >= date_ini]
    data = []
    for c in df.columns:
        data.append(go.Scatter(x=df_final.index, y=df_final.loc[:, c],
                           name = c))
    layout = go.Layout(title="<b>{}</b>".format(title),
                       font=dict(size=18),
                       yaxis=dict(title="% (0=average)", tickmode="auto", nticks="5"),
                       legend=dict(x=0, y=-0.4),
                       showlegend=True,
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14)),
                                    dict(
                                        x=.95,
                                        y= -0.2,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=14, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        opacity=0.5,
                                        showarrow=False
                                    )])


    return go.Figure(data=data, layout=layout)


date_ini = "1995-01-01"
py.image.save_as(gen_chart(df_mid, "Effective Exchange Rate", "%", date_ini),
                 os.path.join(caminho, "real_exchange_rate.jpeg"), format="jpeg")
