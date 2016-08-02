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
trace01 = go.Scatter(x=cf_cycle.index, y=cf_cycle,
                     name= "Output Gap")
data = [trace01]
layout = go.Layout(title="<b>Output Gap-Brazil</b",
                   font=dict(size=18),
                   yaxis=dict(title="%Trend"))
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, "../exhibits/outputgap.jpeg", format="jpeg")
