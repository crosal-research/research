import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

# Load Data
caminho = "/home/jmrosal/Documents/crosal/research/research/data/{}"
caminho1 = "/home/jmrosal/Documents/crosal/research/ff_probability/data/output/{}"

ds = pd.read_csv(caminho.format("stock_markets.csv"), index_col=0)
df = pd.read_csv(caminho.format("brlusd.csv"), index_col=0)
dm = pd.merge(ds, df, left_index=True, right_index=True, how="outer")

# normalization in usd for stock markets
dm["^BVSP"] = dm["^BVSP"] / dm["BRLUSD"]
dm.columns = ["Ibovespa", "S&P", "BRlUSD"]


### chart
def gen_chart(df, title, y_title, date_ini, source=True):
    df_final = df[df.index >= date_ini]
    col = np.array(["#000099", "#ff9900"])
    data = []
    for c in df_final.columns:
        if c == "Ibovespa":
            data.append(go.Scatter(x=df_final.index, y=df_final.loc[:, c].values,
                                   name=c,
                                   marker=dict(color=col[df_final.columns==c])))
            data.append(go.Scatter(x=df_final.tail(1).index,
                                   y=df_final.tail(1).loc[:, c].values,
                                   marker=dict(color=col[df_final.columns==c]),
                                   showlegend=False,
                                   mode="markers+text",
                                   text=["<b>"+str(round(df_final.tail(1).loc[:, c].values[0], 1))+"</b>"],
                                   textposition='top',
                                   textfont=dict(size=14)))
        else:
            data.append(go.Scatter(x=df_final.index, y=df_final.loc[:, c].values,
                                   name=c,
                                   marker=dict(color=col[df_final.columns==c]), yaxis='y2'))
            data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).loc[:, c],
                                   marker=dict(color=col[df_final.columns==c]), showlegend=False,
                                   mode="markers+text",
                                   text=["<b>"+str(round(df_final.tail(1).loc[:, c].values[0], 1))+"</b>"],
                                   textposition='top',
                                   textfont=dict(size=14), yaxis='y2'))



    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title=y_title, tickmode="auto", nticks=5,
                                  tickfont=dict(size=16)),
                       yaxis2=dict(title=y_title, tickmode="auto", nticks=5,
                                   tickfont=dict(size=16), side='right',
                                   overlaying='y'),
                       xaxis=dict(tickfont=dict(size=16)),
                       legend=dict(x=0, y=-0.4, font=dict(size=16)),
                       font=dict(size=18))
                       # annotations=[dict(x=df.tail(1).index.values[0],
                       #                   y=df.max().max(),
                       #                   xref='x',
                       #                   yref='y',
                       #                   text="<b>"+ pd.to_datetime(df_final.tail(1).index).strftime("%m-%d-%Y")[0]+"</b>",
                       #                   font=dict(size=14))])
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

date_ini = "2006-01-05"
fig = gen_chart(dm.loc[:, ["Ibovespa", "S&P"]].dropna(), "Ibovespa (USD) x S&P", "Pts", date_ini)
py.image.save_as(fig, "../exhibits/ibovusd.jpeg")
