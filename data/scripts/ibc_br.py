######################################################################
# script do retrive ibc-br series from webservice
# initial date: 14/07/2016
######################################################################
import pandas as pd
from bcb import *
from datetime import datetime

series = {"24363":"ibc_br", "24364":"ibc_br_sa"}

today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), "01/01/2003", today)
df.columns = [series[s] for s in df.columns]
df.to_csv("../ibc_br.csv", header=True, index=True)
