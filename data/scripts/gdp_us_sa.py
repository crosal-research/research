######################################################################
# script to fetch gdp data for us from fred
# intial date: 08/4/2016
######################################################################
import pandas as pd
import os
from fred import *

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series = ["GDPC1"]
df = fetch_fred(series)
df.to_csv(os.path.join(caminho, "gdp_us_sa.csv"), header=True, index=True)
