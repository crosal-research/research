######################################################################
# retrieves credit quality info on non-earmarked from BCB webservices
# initial date: 14/07/2016
######################################################################p
import pandas as pd
from bcb import *
from datetime import datetime

series = {"21085":"total_del", "21086":"companies_del", "21112": "households_del",
          "21006": "total_late", "21007": "companies_late", "21008": "households_late",
          "20717": "total_juros", "20718":"companies_juros", "20740": "households_juros",
          "20786": "total_spread", "20787": "companies_spread", "20809": "households_spread"}


today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), '01/03/2011', today)


df.columns = [series[s] for s in df.columns]
df.to_csv('../credit_quality.csv', header=True, indexo=True)
