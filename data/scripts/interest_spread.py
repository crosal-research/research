######################################################################
# Script to download from finnacloud interest rate spread.
# Initial date: 28/06/2016
####################################################################
import bcb
import json, os
import pandas as pd
from datetime import datetime


series = {"1178":"Selic rate", "7801":"cdi1m", "7802": "cdi2m", "7805":"cd16m",
          "7806": "cdi1h"}

today = datetime.today().strftime("%d/%m/%Y")

df = bcb.fetch_bcb(series.keys(), "01/01/2010", today)
df.columns = [series[n] for n in df.columns]

df.to_csv('../interest_spread.csv', header=True, index=True)
