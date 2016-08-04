######################################################################
# script to fetch US interest rates from fred api
# initial date: 08/07/2016
######################################################################
from fred import *
import pandas as pd


series = ["DGS10", "DGS5", "DGS2", "DFF"]
df = fetch_fred(series)

df.to_csv("../interest_rates_us.csv", index=[0], header=True)
