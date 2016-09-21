####################################################################
# script to draw chart of 10 years us treasury
# initial data: 08/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('../data/interest_rates_us.csv', index_col=[0],
                 usecols=[0,1], na_values=["NaN", "."]).dropna()



## chart

def chart_gen(df, title, y_title, leg, data_ini, source=True):
    df_final = df[df.index >= data_ini]
    trace01 = go.Scatter(x=df_final.index, y=df_final.iloc[:, 0],
                         name=leg[0], showlegend=False)
    data = [trace01]
    layout = go.Layout(title="<b>{}</b>".format(title),
                       font=dict(size=18),
                       yaxis=dict(title="{}".format(y_title),
                                  tickmode="auto", nticks=5),
                       legend=dict(x=0, y=-0.4),
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14))])

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
            showarrow=False)]))


    return go.Figure(data=data, layout=layout)


# generates charts
start_date = "2005-00-01"
py.image.save_as(chart_gen(df, "10 Years US Treasury", "%annual",
                           ["10 Years Treasury"],
                           start_date),
                 "../exhibits/10yrs_interest_us.jpeg", format="jpeg")
