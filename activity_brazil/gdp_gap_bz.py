######################################################################
# script to draw output gap for Brazil
# initial date: 08/02/2016
#####################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import statsmodels.api as sm


df = pd.read_csv("../data/gdp_sa_categories.csv", index_col=0)
df_gdp = df.iloc[:, 1]
cf_cycle, cf_trend = sm.tsa.filters.cffilter(df_gdp,
                                             low=4,
                                             high=24,
                                             drift=True)

##draw chart for GDP gap
def gap_fig(df_input, title, y_title, date_ini, source=True):
    df = df_input[df_input.index >= date_ini]
    df_last = df.tail(1)
    trace01 = go.Bar(x=df.index, y=df,
                     name=title)
    trace02 = go.Scatter(x=df_last.index, y=df_last,
                         mode="markets+text",
                         text=["<b>"+str(round(df_last.values[0]))+"</b>"],
                         textposition='bottom', showlegend=False, textfont=dict(size=16))
    data = [trace01, trace02]
    layout = go.Layout(title="<b>{}</b>".format(title),
                       font=dict(size=22),
                       yaxis=dict(title="{}".format(y_title)),
                       showlegend=False,
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()-5,
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=16)),
                                    dict(
                                        x=.95,
                                        y= -0.2,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=16, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        opacity=0.5,
                                        showarrow=False
                                    )])

    return go.Figure(data=data, layout=layout)


py.image.save_as(gap_fig(cf_cycle, "Output Gap", "%trend", "2010-01-01"),
                 "../exhibits/outputgap.jpeg", format="jpeg")
