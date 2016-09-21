######################################################################
# script do retrive ibc-br series from webservice
# initial date: 14/07/2016
######################################################################
import pandas as pd
import os
from bcb import *
from datetime import datetime

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series = {"24363":"ibc_br", "24364":"ibc_br_sa"}

today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), "01/01/2003", today)
df.columns = [series[s] for s in df.columns]
df.to_csv(os.path.join(caminho, "ibc_br.csv"), header=True, index=True)
