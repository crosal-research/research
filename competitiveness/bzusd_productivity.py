######################################################################
# draw chart for unit labor cost
# initial date: 04/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/"

df = pd.read_csv(os.path.join(caminho, 'data/cut.csv'), index_col=0, usecols=[0,1])
n = [1.0 for i in range(0, df.size)]
df_ave = pd.DataFrame(n, index=df.index, columns = ['average']) * df.mean()[0]
df_mid = pd.merge(df, df_ave, left_index=True, right_index=True, how="inner")


def gen_chart(df, title, y_title, date_ini, source=True):
    df_final = df[df.index >= date_ini]
    data = []
    for c in df.columns:
        if c != "average":
            data.append(go.Scatter(x=df_final.index, y=df_final.loc[:, c],
                                   name = c))
        else:
            data.append(go.Scatter(x=df_final.index, y=df_final.loc[:, c],
                                   name = c, line=dict(color="red", dash="dot")))

    layout = go.Layout(title="<b>{}</b>".format(title),
                       font=dict(size=18),
                       yaxis=dict(title="{}".format(y_title), tickmode="auto", nticks="5"),
                       legend=dict(x=0, y=-0.6),
                       showlegend=True,
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()*(0.8),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14))])
    if source:
        layout.update(dict(annotations=[dict(
            x=.95,
            y= -0.6,
            xref='paper',
            yref='paper',
            text="<b><i>CRosal Independent Research</i></b>",
            font=dict(size=14, family='Courier new', color="#ffffff"),
            bgcolor='#ff8080',
            opacity=0.5,
            showarrow=False
        )]))


    return go.Figure(data=data, layout=layout)

date_ini = "1995-01-01"
fig = gen_chart(df_mid, "Deflated Labor Productiity in USD" , "% (100=average)", date_ini)
py.image.save_as(fig, os.path.join(caminho, 'exhibits/usdbr_productivity.jpeg'),
                 format="jpeg")
