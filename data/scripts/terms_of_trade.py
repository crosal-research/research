######################################################################
# script to fetch data about terms of trade for Brazil from ipeadata
# initial date: 04/07/2016
######################################################################
import pandas as pd

## url for the data
url = "http://www.ipeadata.gov.br/ExibeSerie.aspx?oper=exportCSVBr&"
url = url + "serid35681=35681&serid35584=35584"
df = pd.read_csv(url, sep = ";", usecols=[0, 1, 2],
                 parse_dates=[0], decimal=",", index_col=0).dropna()
df.columns = ['import', 'export']

## save data
df.to_csv('../terms_of_trade.csv', index=True, header=True)
