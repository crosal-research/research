import ibge
import os
import pandas as pd


caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

tables = ['6381', '6380']

## Data to fetch umployment rate
url = "http://www.sidra.ibge.gov.br/api/values/t/6381" + \
      "/p/all/v/4099/n1/1/f/a/h/n"


##fetch data
df = pd.read_json(url, convert_dates=['D1N']).loc[:, ['D1N', 'V']].set_index('D1N')
df.index = pd.date_range(start="2012-03-01", periods=len(df.index), freq="MS")
df.index.name = "Date"
df.columns = ['Unemploymnet Rate']
#df.to_csv(os.path.join(caminho,"labor_market_bz.csv"))


## Data to fetch participation ration
url1 = "http://www.sidra.ibge.gov.br/api/values/t/5944" + \
      "/p/all/v/4096/n1/1/f/a/h/n"


##fetch data
df1 = pd.read_json(url1, convert_dates=['D1N']).loc[:, ['D1N', 'V']].set_index('D1N')
df1.index = pd.date_range(start="2012-03-01", periods=len(df1.index), freq="MS")
df1.index.name = "Date"
df1.columns = ['Participation Rate']


## Data to fetch participation ration
url2 = "http://www.sidra.ibge.gov.br/api/values/t/6390" + \
      "/p/all/v/5933/n1/1/f/a/h/n"


##fetch data
df2 = pd.read_json(url2, convert_dates=['D1N']).loc[:, ['D1N', 'V']].set_index('D1N')
df2.index = pd.date_range(start="2012-03-01", periods=len(df1.index), freq="MS")
df2.index.name = "Date"
df2.columns = ['real wages']

## save data
dfinal = pd.merge(df, df1, left_index="True", right_index="True", how='inner')
dfinal= pd.merge(dfinal, df2, left_index="True", right_index="True", how="inner")
dfinal.to_csv(os.path.join(caminho, "labor_market_month_bz.csv"),
              index=True, header=True)
