######################################################################
# script to retrieve fiscal series for Brazil from BCB webservices
# initial date: 13/07/2016
######################################################################
from bcb import *
from datetime import datetime
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series = {'13762': "gross_debt_gdp",
          '5727': "total_balance_gdp",
          '5760': 'interest_gdp',
          '5793': "primary_gdp"}


today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), '01/01/2003', today)
df.columns = [series[s] for s in df.columns]
df.to_csv(os.path.join(caminho, 'fiscal_policy.csv'), index=True)
