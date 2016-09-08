######################################################################
# fetch stock market data from yahoo
#
######################################################################
from yahoo import *
import pandas as pd
from datetime import datetime


series=["^BVSP", "^GSPC"]
date_ini = "01/01/2011"
today = datetime.today().strftime("%m/%d/%Y")

df = fetch_yahoo(series, date_ini, today).dropna()
df.to_csv("../stock_markets.csv", header=True, index=True)
