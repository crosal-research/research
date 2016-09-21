######################################################################
# script to retrieve Itf's implicy volatilities
# initial date: 13/07/2016
######################################################################
from fred import *
import pandas as pd
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series = ["VIXCLS","VXEEMCLS", "VXEWZCLS"]

df = fetch_fred(series)
df.to_csv(os.path.join(caminho, "stock_vol_imp.csv"), header=True, index_col=True)
