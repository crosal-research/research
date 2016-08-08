######################################################################
# Chart for interest rates sprads
# initial date: 28/06/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/interest_spread.csv", header=0, index_col=0,
                 usecols=[0, 1,4,5]).dropna()

## chart


def chart_gen(df, title, y_title, leg, data_ini):
    df_cut = df[df.index >= start_date]
    data = []
    for i in range(0, len(df.columns)):
        trace = go.Scatter(x=df_cut.index, y=df_cut.iloc[:,i], name=leg[i])
        data.append(trace)
    layout = go.Layout(title="<b>{}</b>".format(title),
                       yaxis=dict(title="{}".format(y_title), tickmode="auto", nticks=5),
                       font=dict(size=18), legend=dict(x=0, y=-0.4))
    return go.Figure(data=data, layout=layout)


#generate chart
start_date = "2016-01-01"
py.image.save_as(chart_gen(df, "Interest Rate Term Structure",
                           "%p.y.", ["Selic", "6M Interbank", "1Y interbank"],
                           start_date), '../exhibits/interest_spreads.jpeg', format="jpeg")
