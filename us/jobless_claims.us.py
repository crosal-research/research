######################################################################
# script to draw chart on us cpi
# initial date: 15/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go



df = pd.read_csv("../data/jobless_claims_us.csv", index_col=[0]).dropna()
df.columns = ["Jobless Claim", "4-week moving average"]


def gen_chart(df, title, y_title, leg, date_ini, source=True):
    df_final = df[df.index >= date_ini]
    data = []
    col = ["#00cc00", "#ff9900", "black"]
    for i in range(0, len(df.columns)):
        pos = "bottom-left"
        data.append(go.Scatter(x=df_final.index, y=df_final.iloc[:, i], name=leg[i],
                    marker=dict(color=col[i])))
        data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).iloc[:,i],
                    mode="markers+text",
                    text=["<b>"+str(round(df_final.tail(1).iloc[:, i].values[0], 0))+"</b>"],
                               textposition=pos, showlegend=False,
                               marker=dict(color=col[i]),
                               textfont=dict(color=col[i])))
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title=y_title), font=dict(size=18),
                       legend=dict(x=0, y=-0.4))

    if source:
        layout.update(dict(annotations=[dict(
            x=.95,
            y= -0.4,
            xref='paper',
            yref='paper',
            text="<b><i>CRosal Independent Research</i></b>",
            font=dict(size=14, family='Courier new', color="#ffffff"),
            bgcolor='#ff8080',
            opacity=0.5,
            showarrow=False
        )]))

    return go.Figure(data=data, layout=layout)


py.image.save_as(gen_chart(pd.DataFrame(df.iloc[:, 1]), "Jobless Claims", "% yoy", df.columns,
                           "1980-01-10"), "../exhibits/Jobless_claims_us.jpeg", format="jpeg")
