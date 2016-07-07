######################################################################
# fetch data for unit labor cost, Brazil
# initial date: 04/07/2016
######################################################################
from fred import *


series = ['ULCMFG']

df = fetch_fred(series)
df.columns = ["cut"]

## save onto the disk
df.to_csv("../cut_us.csv", header=True, index=True)
