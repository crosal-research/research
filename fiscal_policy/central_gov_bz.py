######################################################################
# script to draw charts about central gov. fiscal accounts
# initial date: 28/07/2016
# comments: still very incomplete
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/primary_surplus.csv", index_col=0)

## Primary Surplus (real)
dipca = pd.DataFrame((df['IPCA']/100 + 1).cumprod())
dipca = dipca.div(dipca.tail(1).ix[0], axis=1)
dreal = df.iloc[:,:-2].div(dipca.iloc[:,0], axis=0)
dspreal = dreal.iloc[:, [0, 33, 34, 70]]

## Primary Surplus (GDP ratio)
df_sum = df.rolling(window=12).sum()
df_gdp = df_sum.iloc[:, :-2].div(df_sum.loc[:, 'GDP'], axis=0)*100
