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
cf_cycle, cf_trend =sm.tsa.filters.cffilter(df_gdp,
                                            low=4,
                                            high=24,
                                            drift=True)

##draw chart for GDP gap
def gap_fig(df_input, title, y_title, date_ini):
    df = df_input[df_input.index >= date_ini]
    trace01 = go.Bar(x=df.index, y=df,
                     name= title)
    data = [trace01]
    layout = go.Layout(title="<b>{}</b>".format(title),
                       font=dict(size=18),
                       yaxis=dict(title="{}".format(y_title)))
    return go.Figure(data=data, layout=layout)


py.image.save_as(gap_fig(cf_cycle, "Output Gap", "%trend", "2010-01-01"),
                 "../exhibits/outputgap.jpeg", format="jpeg")
