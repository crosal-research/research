######################################################################
# script to draw chart with us' gdp sa data
# initial date: 04/08/2016
#####################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/gdp_us_sa.csv", index_col=[0],
                 na_values=["."])
df_ch = df.pct_change(periods=1)*100*4


def chart_gen(df, title, y_title, leg, date_ini, source=True):
    '''
    imputs:
    - df: dataframe
    - title: string
    - y_title: string
    - leg: [string]
    - date_ini: string
    output:
    - pyplot figure.
    '''
    df_final = df[df.index >= date_ini]
    trace0 = go.Bar(x=df_final.index, y=df_final.iloc[:, 0],
                    name=leg[0], showlegend=False)
    data = [trace0]
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title=y_title), font=dict(size=18))


    if source:
        layout.update(dict(annotations=[dict(
            x=.95,
            y= -0.2,
            xref='paper',
            yref='paper',
            text="<b><i>CRosal Independent Research</i></b>",
            font=dict(size=14, family='Courier new', color="#ffffff"),
            bgcolor='#ff8080',
            opacity=0.5,
            showarrow=False
        )]))

    return go.Figure(data=data, layout=layout)


start_date = "2013-01-01"
py.image.save_as(chart_gen(df_ch, "GDP US (sa)", "qoq% <br> (annualized)", ["GDP US"], start_date),
                 "../exhibits/gdp_sa_us_chart.jpeg", format="jpeg")
