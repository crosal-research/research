######################################################################
# fetch stock market data from yahoo
#
######################################################################
from yahoo import *
import pandas as pd
import os
from datetime import datetime

#
caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series=["^BVSP", "^GSPC"]
date_ini = "01/01/2003"
today = datetime.today().strftime("%m/%d/%Y")

df = fetch_yahoo(series, date_ini, today).dropna()
df.to_csv(os.path.join(caminho, "stock_markets.csv"), header=True, index=True)
