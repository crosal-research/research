######################################################################
# fetch data for effective exchange rate, Brazil
# initial date: 05/07/2016
######################################################################
import bcb
import pandas as pd
from datetime import datetime
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

series = {'11752':"fx_real", '11776':"fx_prod"}

date_ini = "31/01/1989"
today = datetime.today().strftime("%d/%m/%Y")

df = bcb.fetch_bcb(series.keys(), date_ini, today)
df.columns = [series[k] for k in series]
df.to_csv(os.path.join(caminho, "real_fx_rate.csv"), header=True, index=True)
