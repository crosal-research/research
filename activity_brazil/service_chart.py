######################################################################
# spript to draw service chart
# initial data: 15/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv("../data/servicos_brazil_sa.csv", index_col = [0])
df_col = pd.merge(pd.DataFrame(df.iloc[:, 3]),
                  pd.DataFrame(df.iloc[:,3].rolling(window=3).mean()),
                  left_index=True, right_index=True,
                  how="inner").pct_change(periods=1)*100
df_col.columns = ["services", "3M ma"]


def gen_chart(df, title, y_title, leg, date_ini, source=True):
    '''
    '''
    df_final = df[df.index >= date_ini]
    data = []
    for i in range(len(df_final.columns)):
        if i == 0:
            dat = go.Scatter(x=df_final.index, y=df_final.iloc[:, i],
                             name=leg[i])
            data.append(dat)
        else:
            dat = go.Bar(x=df_final.index, y=df_final.iloc[:, i],
                             name=leg[i])
            data.append(dat)
        trace01 = go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1)['services'],
                             mode="markers+text",
                             text=["<b>"+str(round(df_final.tail(1)['services'].values[0], 1))+"</b>"],
                             textposition='leftl', showlegend=False)
        data.append(trace01)
        layout = go.Layout(title="<b>{}</b>".format(title),
                           font=dict(size=18),
                           legend=dict(x=0, y=-0.4),
                           yaxis=dict(title=y_title,
                                      tickmode="auto", nticks=5),
                           annotations=[dict(x=df_final.tail(1).index.values[0],
                                         y=df_final.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df_final.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=16)),
                                    dict(
                                        x=.95,
                                        y= -0.4,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=16, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        opacity=0.5,
                                        showarrow=False
                                    )])

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

date_start = "2015-09-01"
py.image.save_as(gen_chart(df_col, "Service Sector",
                           "%momsa", df_col.columns, date_start),
                 "../exhibits/service_sa.jpeg", format="jpeg")
