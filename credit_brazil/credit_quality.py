######################################################################
# script to draw charts on credit quality
# initial date 14/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/credit_quality.csv", header=0, index_col=0)


## function to produce charts
def gen_chart(df, title, y_title, date_ini):
    """"""
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
                               textposition='top',
                               textfont=dict(size=14)))

    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title=y_title, tickmode="auto", nticks=5),
                       legend=dict(x=0, y=-0.4),
                       font=dict(size=18),
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14))])
    return go.Figure(data=data, layout=layout)


## chart on credit quality
df_qual = df.loc[:, ['total_del', 'companies_del', 'households_del']]
df_qual.columns = ["Total", "Companies", "Households"]
date_qual = '2012-01-01'
py.image.save_as(gen_chart(df_qual, "Deliquencies", "%Credit Class",
                           date_qual),
                 "../exhibits/credit_quality.jpeg",
                 format="jpeg")


## chart on interest rate
df_int = df.loc[:, ['total_juros', 'companies_juros', 'households_juros']]
df_int.columns = ["Total", "Companies", "Households"]
date_int = '2012-01-01'
py.image.save_as(gen_chart(df_int, "Interest Rates", "%Credit Class",
                           date_int),
                 "../exhibits/credit_interest.jpeg",
                 format="jpeg")
