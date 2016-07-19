######################################################################
# script to draw charts for Brazil's credit volume
# initial date: 14/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df = pd.read_csv('../data/credit_volume.csv', index_col=0)
df_ch = df.pct_change(periods=12)*100
df_12m = df.rolling(window=12).sum().dropna()
df_gdp = df_12m.div(df_12m['GDP'], axis=0).iloc[:,1:]*10


def credit_volume(df_gdp, new_date, title):
    df_gdp_new = df_gdp[df_gdp.index >= new_date]
    names = df_gdp.columns
    ## volume
    trace01 = go.Scatter(x=df_gdp_new.index, y=df_gdp_new['Total'],
                         name=names[0])
    trace02 = go.Scatter(x=df_gdp_new.index, y=df_gdp_new['Institutions'],
                         name=names[1])
    trace03 = go.Scatter(x=df_gdp_new.index, y=df_gdp_new['Households'],
                         name=names[2])
    data0 = [trace01, trace02, trace03]
    layout0 = go.Layout(title="<b>{}</b>".format(title),
                        yaxis=dict(title="%GDP", tickmode="auto", nticks=5),
                        font=dict(size=18),
                        legend=dict(x=0, y=-0.4))
    return go.Figure(data=data0, layout=layout0)

py.image.save_as(credit_volume(df_gdp, "2010-01-01", "Credit Volume - Brazil" ),
                 '../exhibits/credit_gdp_chart.jpeg', format="jpeg")
