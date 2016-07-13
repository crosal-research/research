######################################################################
# script to retrieve Itf's implicy volatilities
# initial date: 13/07/2016
######################################################################
from fred import *
import pandas as pd

series = ["VIXCLS","VXEEMCLS", "VXEWZCLS"]

df = fetch_fred(series)
df.to_csv("../stock_vol_imp.csv", header=True, index_col=True)
