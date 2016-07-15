######################################################################
# script to download financial stability data from BCB's webservice
# initial date: 15/07/2016
######################################################################
from bcb import *
import pandas as pd
from datetime import datetime


series = {"21424": "basel_index", "21425": "leverage_ratio",
          "21509": "liquidty_index", "21439":"ROE"}

today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), "01/01/2001", today)
df.columns = [series[s] for s in df.columns]


df.to_csv("../financial_stability_bz.csv", header=True, index=True)
