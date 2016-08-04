######################################################################
# script to fetch gdp data for us from fred
# intial date: 08/4/2016
######################################################################
import pandas as pd
from fred import *

series = ["GDPC1"]
df = fetch_fred(series)
df.to_csv("../gdp_us_sa.csv", header=True, index=True)
