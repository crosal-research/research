from ibge import *
import pandas as pd

address_ch = "http://www.sidra.ibge.gov.br/api/values/t/1419" + \
             "/p/all/v/63/c315/{}/n7/7/f/a"

req = address_ch.format("7448")

df = pd.DataFrame(ibge_fetch([req], freq="M"))

df.to_csv('aluguel.csv', index=True, header=True)

df_new = pd.read_csv('aluguel.csv', index_col = 0)

df_yoy = (1 + df_new/100).cumprod().pct_change(periods=12)*100
