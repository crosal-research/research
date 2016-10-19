######################################################################
# script to compare dynamics of IPA-DI and IPCA
# inital date: 18/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# fetch data
pd_igp = pd.read_csv('../data/igpdi.csv', index_col=[0])
pd_ipca = pd.read_csv('../data/cpi_core_bz.csv', index_col=[0],
                      usecols=[0, 1])

df = pd.merge(pd_igp, pd_ipca, left_index=True, right_index=True, how='outer').dropna()
df_yoy = ((df/100 + 1).cumprod().pct_change(periods=12)*100)
df_final = df_yoy.loc[:,["IPAIND", "IPAG", "cpi"]].dropna()
df_final.columns = ["WPI - Agriculture", "WPI - Industry", "CPI"]



def gen_chart(df, title, y_title, date_ini, source=True):
    df_final = df[df.index >= date_ini]
    col = ["#000099", " #ff9900", "#00cc00"]
    data = []
    for i in range(0, len(df.columns)):
        data.append(go.Scatter(x=df_final.index, y=df_final.iloc[:, i],
                               name=df.columns[i],
                               marker=dict(color=col[i])))
        data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).iloc[:, i],
                               marker=dict(color=col[i]), showlegend=False,
                               mode="markers+text",
                               text=["<b>"+str(round(df_final.tail(1).iloc[:, i].values[0], 1))+"</b>"],
                               textposition='top right',
                               textfont=dict(size=14)))

    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title=y_title, tickmode="auto", nticks=5,
                                  tickfont=dict(size=16), range = [0, 40]),
                       xaxis=dict(tickfont=dict(size=16)),
                       legend=dict(x=0, y=-0.4, font=dict(size=16)),
                       font=dict(size=18),
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max() -10,
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df_final.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14)),
                                    dict(
                                        x=.98,
                                        y=-0.4,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=14, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        showarrow=False)])

    return go.Figure(data=data, layout=layout)

# generate chart
date_ini = "2013-01-01"
fig = gen_chart(df_final, "Inflation Dynamics", "yoy%", date_ini, source=True)
py.image.save_as(fig, "../exhibits/inflation_dynamics_bz.jpeg", format="jpeg")
