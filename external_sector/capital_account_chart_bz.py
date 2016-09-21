######################################################################
# draw data on capital account data
# initial date: 21/07/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("../data/net_capital_flow.csv", index_col=0)
df_sum = df.rolling(window=12).sum()


## chart
def gen_chart(df, title, y_title, date_ini, source=True):
    '''
    Produces plot.ly figure from a dataframe, the title, y title,
    initial date and add crosal label.
    inputs:
    ------
    - df: Dataframe
    - tittle: str
    - y_title: str
    - date_ni: str (ex: Y%-%m-%d)
    -source: boolean
    Outputs:
    -------
    - plot.ly figure
    '''
    df_final = df[df.index >= date_ini]
    data = []
    # Choose colors from http://colorbrewer2.org/ under "Export"
    color = np.array(['rgb(166,206,227)','rgb(31,120,180)','rgb(178,223,138)',
             'rgb(51,160,44)','rgb(251,154,153)','rgb(227,26,28)',
             'rgb(253,191,111)','rgb(255,127,0)','rgb(202,178,214)',
             'rgb(106,61,154)','rgb(255,255,153)','rgb(177,89,40)'])
    for c in df_final.columns:
        data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).loc[:, c],
                               marker=dict(color=color[df.columns == c][0]),
                               showlegend=False, mode="markers+text",
                               text=["<b>"+str(round(df_final.tail(1).loc[:, c].values[0], 1))+"</b>"],
                               textposition='top left',
                               textfont=dict(size=14)))
        dat = go.Scatter(x=df_final.index, y=df_final.loc[:, c],
                         name=c, marker=dict(color = color[df.columns == c][0]))
        data.append(dat)

    layout = go.Layout(title="<b>{}</b>".format(title),
                       font=dict(size=18),
                       yaxis=dict(title=y_title, tickmode="auto", nticks=5),
                       legend=dict(x=0, y=-0.4),
                       annotations=[dict(x=df_final.tail(1).index.values[0],
                                         y=df_final.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df_final.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14)),
                                    dict(
                                        x=.95,
                                        y= -0.4,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=14, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        opacity=0.5,
                                        showarrow=False
                                    )])

    return go.Figure(data=data, layout=layout)



# total
date_ini = "2001-01-01"
df_net = df_sum.loc[:, ["net_financial_account", "net_fdi", "net_portfolio_flow"]]
df_net.columns = ["Financial Accounts", "Net FDI", "Net Porfolio Flow"]
fig = gen_chart(df_net, "Net Financial Account", "USDmn", date_ini)
py.image.save_as(fig, "../exhibits/net_capital_flow.jpeg",format="jpeg")


# # FDI
# py.image.save_as(net_flow("2010-01-01", ["net_fdi"], "Net FDI",
#                           ytitle="USDmn"),
#                 "../exhibits/net_fdi.jpeg",format="jpeg")

# # Capital Inflow
# py.image.save_as(net_flow("2010-01-01", ["net_portfolio_flow"], "Net Portfolio Flow",
#                           ytitle="USDmn"),
#                 "../exhibits/net_portfolio.jpeg",format="jpeg")
