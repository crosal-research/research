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



def gen_chart(df, title, y_title, date_ini, source=True):
    df_final = df[df.index >= date_ini]
    col = ["#000099", " #ff9900", "#00cc00"]
    data = []
    for i in range(0, len(df.columns)):
        data.append(go.Scatter(x=df_final.index, y=df_final.iloc[:, i],
                               name=df.columns[i],
                               marker=dict(color=col[i])))
        data.append(go.Scatter(x=df_final.tail(1).index, y=df_final.tail(1).iloc[:, i],
                               marker=dict(color=col[i]), showlegend=False,
                               mode="markers+text",
                               text=["<b>"+str(round(df_final.tail(1).iloc[:, i].values[0], 1))+"</b>"],
                               textposition='top left',
                               textfont=dict(size=14)))

    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title=y_title, tickmode="auto", nticks=5),
                       legend=dict(x=0, y=-0.4),
                       font=dict(size=18),
                       annotations=[dict(x=df.tail(1).index.values[0],
                                         y=df.max().max()*(1.1),
                                         xref='x',
                                         yref='y',
                                         text="<b>"+ pd.to_datetime(df.tail(1).index).strftime("%b-%Y")[0]+"</b>",
                                         font=dict(size=14))])
    if source == True:
        layout.update(dict(annotations=[dict(
            x=.95,
            y=-0.4,
            xref='paper',
            yref='paper',
            text="<b><i>CRosal Independent Research</i></b>",
            font=dict(size=14, family='Courier new', color="#ffffff"),
            bgcolor='#ff8080',
            opcity=0.5,
            showarrow=False
        )]))

    return go.Figure(data=data, layout=layout)


## Generate chart for households, companies and Total
start_date = "2000-01-01"
py.image.save_as(gen_chart(df_gdp.loc[:,['Total', "Institutions", "Households"]]
                           , "Credit Volume - Brazil", "%GDP", start_date),
                 '../exhibits/credit_gdp_chart.jpeg', format="jpeg")

## Generate chart for earmarked, non-earmarked and Total
start_date = "2000-01-01"
py.image.save_as(gen_chart(df_gdp.loc[:,['Total', "non-earmarked", "earmarked"]]
                           , "Credit Volume - Brazil", "%GDP", start_date),
                 '../exhibits/credit_gdp_earmarked.jpeg', format="jpeg")
