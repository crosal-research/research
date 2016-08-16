######################################################################
# draw charts for high yield spreads
# initial date: 11/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv("../data/high_yields.csv", index_col=[0],
                 na_values=['.'])


def chart_gen(df, title, y_title, leg, date_ini):
    '''
    Generates plotly figure.
    input:
    - df: dataframe
    - title: string
    - y_title: string
    - leg: [string]
    - date_ini
    output:
    - ploly figure object

    '''
    df_final = df[df.index >= date_ini]
    data = []
    for i in range(len(df.columns)):
        dat = go.Scatter(x=df_final.index, y=df_final.iloc[:, i], name=leg[i])
        data.append(dat)
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title="{}".format(y_title),
                                  tickmode="auto", nticks=5,
                                  range=[2, 10]),
                       font=dict(size=18), legend=dict(x=0, y=-0.4))
    brexit = "2016-06-23"
    layout.update(dict(
        shapes=[
            {"type": 'line',
             'xref': 'x',
             'yref': 'y',
             'x0': brexit,
             'y0': 0,
             'x1': brexit,
             'y1': float(df_final.iloc[:, 0].max())+1,
             'line': dict(dash="dot", color="blue")}],
        annotations=[go.Annotation(text="Brexit", x=brexit,
                                   y=float(df_final.iloc[:, 1].max()))]))
    return go.Figure(data=data, layout=layout)



# Yield chart
date_ini = "2016-01-04"
py.image.save_as(chart_gen(df, "High Yield Spreads", "Percent", df.columns, date_ini), "../exhibits/high_yields.jpeg",
                 format="jpeg")
