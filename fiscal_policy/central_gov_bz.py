######################################################################
# script to draw charts about central gov. fiscal accounts
# initial date: 28/07/2016
# comments: still very incomplete
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/central_gov_bz.csv", index_col=0)

## real values
dipca = pd.DataFrame((df['ipca']/100 + 1).cumprod())
dipca = dipca.div(dipca.tail(1).ix[0], axis=1)
df_real = df.iloc[:,2:].div(dipca['ipca'], axis="index")


## GDP
df_sum = df.iloc[:,2:].rolling(window=12).sum()
df_gdp = df_sum.div(df['GDP_monthly'].rolling(window=12).sum(), axis=0).dropna()
