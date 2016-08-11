######################################################################
# script to draw chart for Brazil's nuci
# initial date: 08/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
o
df = pd.read_csv("../data/nuci_bz.csv", index_col=[0], usecols=[0,1])
df_ave = pd.DataFrame(np.ones(len(df))*df.mean()[0], index = df.index)
df_col = pd.merge(df, df_ave, left_index=True, right_index=True, how="inner")

data_start = "2010-01-01"

def gen_chart(df, title, y_title, leg, data_ini):
    '''
    '''
    df_final = df[df.index >= data_ini]
    data = []
    for i in range(len(df_final.columns)):
        trace = go.Scatter(x=df_final.index, y=df_final.iloc[:,i], name=leg[i])
        data.append(trace)
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title="%".format(y_title), tickmode="auto", nticks=5),
                       font=dict(size=18),
                       legend=dict(x=0, y=-0.4))
    return go.Figure(data=data, layout=layout)

py.image.save_as(gen_chart(df_col,
                           "IP's capacity Utilization", "%Total",
                           ["IP's", "Average"], data_start),
                 "../exhibits/ip_nuci_bz.jpeg", format="jpeg")
