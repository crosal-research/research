######################################################################
# script to download balance of payment data from BCB's webservices
# initial date: 13/07/2016
######################################################################p
import pandas as pd
import os
from bcb import *
from datetime import datetime

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series = ['22701', '22702', '22703', '22707', '22708', '22709', '22719', '22720',
          '22721', '4385']
names = ['current_account', 'cc_reveneus', 'cc_spending', 'trade_balance',
         'good_exports', 'good_imports', 'serv_balance', 'serv_exports',
         'serv_imports', 'GDP']

today = datetime.today().strftime("%d/%m/%Y")

d = dict(zip(series, names))
df = fetch_bcb(series, '01/01/1995', today)
df.columns = [d[n] for n in df.columns]
df.to_csv(os.path.join(caminho, 'trade_balance.csv'), header=True, index=True)
