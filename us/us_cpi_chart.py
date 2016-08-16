######################################################################
# script to draw chart on us cpi
# initial date: 15/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/cpi_us.csv", index_col=[0]).dropna()
df_year = df.pct_change(periods=12)*100
df_year.columns = ["CPI", "Core Inflation"]


def gen_chart(df, title, y_title, leg, date_ini):
    df_final = df[df.index >= date_ini]
    data = []
    col = ["#00cc00", "#ff9900"]
    for i in range(0, len(df.columns)):
        data.append(go.Scatter(x=df_final.index, y=df_final.iloc[:, i], name=leg[i],
                    marker=dict(color=col[i])))
        data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).iloc[:,i],
                    mode="markers+text",
                    text=["<b>"+str(round(df_final.tail(1).iloc[:, i].values[0], 1))+"</b>"],
                               textposition='top', showlegend=False,
                    marker=dict(color=col[i])))
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title=y_title), font=dict(size=18),
                       legend=dict(x=0, y=-0.4))
    return go.Figure(data=data, layout=layout)


py.image.save_as(gen_chart(df_year, "CPI Inflation", "% yoy", df_year.columns,
                           "2010-01-10"), "../exhibits/cpi_us.jpeg", format="jpeg")
