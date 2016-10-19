######################################################################
# retrieve data on central government fiscal accounts for BZ
# initial date: 27/07/2016
# last modification: 29/09/2016 - muda fonte para Tesouro Nacional
######################################################################
import pandas as pd
import bcb
from datetime import datetime
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


end = "2016-08-01"
url = "http://www.tesouro.fazenda.gov.br/documents/10180/246449/Anexos+RTN+Ago+2016.xlsx"
xls = pd.ExcelFile(url)

## primary results
dat = pd.date_range(start="1997-01-01", end=end, freq = "MS")
df = (xls.parse('1.1', skiprows=[0, 1, 2, 3], parse_cols=range(0, len(dat)+1),
               skip_footer=5).T)
cols = df.iloc[0, :].apply(lambda x: x.encode('utf-8'))
df = df[df.index != df.index[0]].dropna(how="all")
df.index = dat
df.columns = cols

## Central Bank series
series = {'4380': "GDP", '433': "IPCA"}
today = datetime.today().strftime("%d/%m/%Y")
dc = bcb.fetch_bcb(series.keys(), "01/01/1997", today)
dc.columns = [series[k] for k in dc.columns]

# save data
dfinal = pd.merge(dsp, dc, left_index=True, right_index=True, how='outer')
dfinal.to_csv(os.path.join(caminho, "primary_surplus.csv"), index=True,
                           header=True)
