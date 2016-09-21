######################################################################
# script to download capital account data from BCB's webservices
# initial date: 21/07/2016
# comments:
######################################################################p
import pandas as pd
from bcb import *
from datetime import datetime
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

series = {'22863':"net_financial_account", '22864':'net_fdi', '22905':"net_portfolio_flow",
          '22966':"net_derivatives", '22969':"net_others"}

series_fx ={"13982":"fx_reserves"}

today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), '01/01/1995', today)
df_fx = fetch_bcb(series_fx.keys(), '01/01/2008', today)
df.columns = [series[n] for n in df.columns]
df_fx.columns = [series_fx[n] for n in df_fx.columns]
df.to_csv(os.path.join(caminho, 'net_capital_flow.csv'), header=True, index=True)
df_fx.to_csv(os.path.join(caminho, 'fx_reserves.csv'), header=True, index=True)
