import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df_fx = pd.read_csv('../data/brlusd.csv', index_col=0)
df_ibov = pd.read_csv('../data/stock_markets.csv', index_col=0)
df_ntnf = pd.DataFrame(pd.read_csv('../data/ntnf.csv', parse_dates=[0], index_col=0,
                                   dayfirst=True))[['Base_price']].rename(columns={"Base_price": "NTNF"})
df_ntnb = pd.DataFrame(pd.read_csv('../data/ntnb.csv', parse_dates=[0], index_col=0,
                                   dayfirst=True))[['Base_price']].rename(columns={"Base_price": "NTNB"})

df = pd.merge(df_ibov[["^BVSP"]], df_ntnf,
              left_index=True, right_index=True, how="outer")
df = pd.merge(df, df_ntnb,
              left_index=True, right_index=True, how="outer").dropna()

df_final = df.div(df.iloc[0], axis="columns")


### chart
def gen_chart(df, title, y_title, date_ini, source=True):
    df_final = df[df.index >= date_ini]
    col = ["#000099", " #ff9900", "#000099"]
    data = []
    for i in range(0, len(df.columns)):
        data.append(go.Scatter(x=df_final.index, y=df_final.iloc[:, i].values,
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
                                      tickfont=dict(size=16)),
                           xaxis=dict(tickfont=dict(size=16)),
                           legend=dict(x=0, y=-0.4, font=dict(size=16)),
                           font=dict(size=18),
                           annotations=[dict(x=df.tail(1).index.values[0],
                                             y=df.max().max(),
                                             xref='x',
                                             yref='y',
                                             text="<b>"+ pd.to_datetime(df_final.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                             font=dict(size=14))])
        if source == True:
            layout.annotations.append(dict(
                x=.98,
                y=-0.4,
                xref='paper',
                yref='paper',
                text="<b><i>CRosal Independent Research</i></b>",
                font=dict(size=14, family='Courier new', color="#ffffff"),
                bgcolor='#ff8080',
                showarrow=False
            ))
            return go.Figure(data=data, layout=layout)

date_ini = "2016-01-05"

fig = gen_chart(pd.DataFrame(df_final[["^BVSP"]], "Ibovespa (USD)", "Pts", date_ini))

# fig = go.Figure(data=[go.Scatter(x=df_final.index, y=df_final.loc[:, "Ibov"].values)],
#                 layout=go.Layout(title="text"))

py.image.save_as(fig, "../exhibits/long_term_inv.jpeg")
