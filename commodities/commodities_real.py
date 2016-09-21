#####################################################################
# draw chart on commodities from imf and cpi from fred
# initial date: 15/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

df_com = pd.read_csv("../data/commodity_imf.csv", index_col = [0])
df_cpi = pd.read_csv("../data/cpi_us.csv", index_col = [0],
                      usecols=[0, 1])
df_cpi_n = df_cpi / df_cpi.tail(1).values[0]
df_cpi_d = df_cpi_n[df_cpi_n.index >= df_com.head(1).index[0]]

df_defl = df_com.loc[:, ['PNRG_Index',
                      'PNFUEL_Index', 'PALLFNF_Index']].div(df_cpi_d.iloc[:,0],
                                                            axis='index').dropna()
df_final = (df_defl.div(df_defl.mean(), axis = 'columns') - 1)*100
df_final.columns = ["Fuel", "Non-Fuel", "All Index"]

def gen_chart(df, title, y_title, leg, date_ini, source=True):
    col = ["#000099", " #ff9900", "#00cc00"]
    data = []
    df_final = df[df.index >= date_ini]
    for i in range(0, len(df.columns)):
        data.append(go.Scatter(x=df_final.index, y=df_final.iloc[:,i],
                               name=leg[i],
                    marker=dict(color=col[i])))
        data.append(go.Scatter(x=df_final.tail(1).index,
                               y=df_final.iloc[:, i].tail(1),
                               showlegend=False,
                    marker=dict(color=col[i])))
    layout = go.Layout(title="<b>{}</b>".format(title), yaxis=dict(title=y_title),
                       font=dict(size=22), legend=dict(x=0, y=-.4),
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()*(0.8),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
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
                                        showarrow=False)])


    return go.Figure(data=data, layout=layout)

# Generate chart
date_start = "2010-01-01"
py.image.save_as(gen_chart(df_final, "Commidity Prices - US CPI Deflated",
                           "%Deviation from average", df_final.columns,
                           date_start), "../exhibits/commodities_imf.jpeg",
                 format="jpeg")
