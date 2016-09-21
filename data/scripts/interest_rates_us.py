######################################################################
# script to fetch US interest rates from fred api
# initial date: 08/07/2016
######################################################################
from fred import *
import pandas as pd
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

series = ["DGS10", "DGS5", "DGS2", "DFF"]
df = fetch_fred(series)

df.to_csv(os.path.join(caminho,"interest_rates_us.csv"), index=[0], header=True)
