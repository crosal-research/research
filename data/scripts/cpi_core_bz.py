######################################################################
# script to retrieve data on core cpi for Brazil
# intial date: 15/07/2016
######################################################################
from bcb import *
import pandas as pd
from datetime import datetime

series ={"433":"cpi", "4447":"tradables", "4448": "non-tradables",
         "4449": "nonitored", "4466": "core", "11428": "free"}


today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), "01/01/1993", today).dropna()
df.columns = [series[s] for s in df.columns]
df.to_csv("../cpi_core_bz.csv", header=True, index=True)
