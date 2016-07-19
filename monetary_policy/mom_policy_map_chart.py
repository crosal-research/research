# coding: utf-8

######################################################################
# Chart of the Monetary policy credibility map
# initial date: 31/06/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


## fetch data
df_exp = pd.read_csv('../data/expected.csv', index_col = 0, decimal=",", parse_dates=[0],
                     dayfirst=True)
df_inf = pd.read_csv('../data/mom_policy_map.csv', index_col=0)



def mon_map(df_exp, df_inf, new_date, last_meeting, daily=True):
    '''
    returns plot.ly figure with credibility map for the Brazilian Central Bank
    Input:
    - new_data: string - new date to restrict data frame span (format: %Y-%m-%d)
    - last_meeting: string - date of the last monetary meeting (format: %Y-%m-%d)
    - daily: bool - if monthly or daily frequency
    Output:
    - return plot.ly fig
    '''
    how = "outer" if daily else "inner"
    df_mid = pd.merge(df_exp, df_inf, left_index=True, right_index=True, how = how)
    df_mid.columns = ['expected', 'ipca', 'core', 'target', 'lower', 'upper']
    df_mid.fillna(method="pad", inplace=True)

    ## restricted dataset
    df_final = df_mid[df_mid.index >= new_date]


    ## chart
    trace01 = go.Scatter(x=df_final.index, y=df_final['ipca'],
                         name="CPI Inflation", line=dict(color="orange"))
    trace02 = go.Scatter(x=df_final.index, y=df_final['target'],
                     name="Target", line=dict(color="red"))
    trace03 = go.Scatter(x=df_final.index, y=df_final['core'],
                     name="Core CPI")
    trace04 = go.Scatter(x=df_final.index, y=df_final['expected'],
                     name="Expeted CPI - One Year Out", line=dict(color="black"))
    trace05 = go.Scatter(x=df_final.index, y=df_final['upper'],
                     name="Upper Limit", line=dict(color="red", dash="dot"),
                     showlegend=False)
    trace06 = go.Scatter(x=df_final.index, y=df_final['lower'],
                     name="Lower Limit", line=dict(color="red", dash="dot"),
                     showlegend=False)
    data = [trace01, trace02, trace03, trace04, trace05, trace06]
    layout = go.Layout(title="<b>Monetary Policy Credibility Map</b>",
                   yaxis=dict(title="%mom", tickmode='auto', nticks=5,
                              tickfont=dict(size=14), showgrid=False),
                   xaxis=dict(showgrid=False, tickfont=dict(size=14),
                              tickangle=-30),
                   font=dict(size=18), legend=dict(x=0, y=-0.6, font=dict(size=14)))

    if daily:
        layout.update(dict(
            shapes=[
                {"type": 'line',
                 'xref': 'x',
                 'yref': 'y',
                 'x0': last_meeting,
                 'y0': 0,
                 'x1': last_meeting,
                 'y1': 11,
                 'line': dict(dash="dot", color="blue")
                }],
            annotations=[go.Annotation(text="Last COPOM", x=last_meeting, y=11)]))
    return go.Figure(data=data, layout=layout)


## render figures.
py.image.save_as(mon_map("2016-02-01", "2016-06-08"), '../exhibits/monetary_pol_map_daily.jpeg', format="jpeg")
py.image.save_as(mon_map("2013-02-01", "2016-06-08", False), '../exhibits/monetary_pol_map_monthly.jpeg', format="jpeg")
