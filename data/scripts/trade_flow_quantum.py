######################################################################
# script to fetch data trade flow's volume for Brazil from ipeadata
# initial date: 07/07/2016
######################################################################
import pandas as pd
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

## url for the data
url = "http://www.ipeadata.gov.br/ExibeSerie.aspx?oper=exportCSVBr&"
url = url + "serid35690=35690&serid35590=35590"
df = pd.read_csv(url, sep = ";", usecols=[0, 1, 2],
                 parse_dates=[0], decimal=",", index_col=0).dropna()
df.columns = ['import', 'export']

## save data
df.to_csv(os.path.join(caminho, 'trade_flow_quantum.csv'), index=True, header=True)
