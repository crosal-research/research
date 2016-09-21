import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
import numpy as np


df = pd.read_csv('../data/gdp_sa_categories.csv', index_col=[0])

df_con = df[['Industry - Total', 'Agriculture', 'Services - Total', 'GDP',
             'Household Consumption', "Public Consumption", "Net Investment",
             'Exports of Goods and Services', 'Imports of Goods and Services']]

df_con_qoq = df_con.pct_change(periods=1)*100



def gen_chart(df, title, y_title, date_ini, source=True):
    df_final = df[df.index >= date_ini]
    col = ["#000099", " #ff9900"]
    data = []
    for i in range(0, len(df.columns)):
        if df.columns[i] != 'GDP':

            data.append(go.Bar(x=df_final.index, y=df_final.iloc[:, i],
                                   name=df.columns[i],
                                   marker=dict(color=col[i])))
            data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).iloc[:, i],
                                   marker=dict(color=col[i]), showlegend=False,
                                   mode="markers+text",
                                   text=["<b>"+str(round(df_final.tail(1).iloc[:, i].values[0], 1))+"</b>"],
                                   textposition='top left',
                                   textfont=dict(size=16)))
        else:
            data.append(go.Scatter(x=df_final.index, y=df_final.iloc[:, i],
                                   name=df.columns[i],
                                   marker=dict(color=col[i])))

            data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).iloc[:, i],
                                   marker=dict(color=col[i]), showlegend=False,
                                   mode="markers+text",
                                   text=["<b>"+str(round(df_final.tail(1).iloc[:, i].values[0], 1))+"</b>"],
                                   textposition='bottom left',
                                   textfont=dict(size=16)))

    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title=y_title, tickmode="auto", nticks=5,
                                  tickfont=dict(size=16)),
                       xaxis=dict(tickfont=dict(size=16)),
                       legend=dict(x=0, y=-0.4, font=dict(size=16)),
                       font=dict(size=22),
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()-5,
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df_final.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14)),
                                    dict(
                                        x=.98,
                                        y=-0.4,
                                        xref='paper',
                                        yref='paper',
                                        text="<b><i>CRosal Independent Research</i></b>",
                                        font=dict(size=14, family='Courier new', color="#ffffff"),
                                        bgcolor='#ff8080',
                                        showarrow=False)])
    return go.Figure(data=data, layout=layout)



## Chart
date_start = '2013-10-01'
py.image.save_as(gen_chart(df_con_qoq[['GDP', "Net Investment"]], "2QGDP", "QoQsa", date_start),
                 "../exhibits/categories_sa.jpeg", format="jpeg")


## Table
vtable = df_con_qoq.tail(2).T
table_data = np.concatenate((vtable.index.values.reshape(9,1),
                             np.round(vtable.values, decimals=2)), axis=1)
table_output = np.concatenate((np.array(['Component', "1Q2016 (qoqsa%)",
                                         '2Q2016 (qoqsa%)']).reshape(1,3), table_data), axis=0)
color_font_row = ["00000" for i in range(0, 10)]
color_font_row[0] = "#ffffff"
color_font_row[4] = 'red'
table = FF.create_table(table_output, font_colors = color_font_row)

for i in range(len(table.layout.annotations)):
    table.layout.annotations[i].font.size = 15.5
py.image.save_as(table, filename= "../exhibits/table_gdp_sa_categories.jpeg", format='jpeg')

## Carry over
df_carry = pd.DataFrame(index= ['2016-04-10', '2016-07-01','2016-10-01'])
df_carry['GDP'] = df['GDP'].tail(1).values[0]
df_carryover = pd.concat([pd.DataFrame(df['GDP']), df_carry]).rolling(window=4).sum().pct_change(periods=4)*100
df_carryover.tail(1)
