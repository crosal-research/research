######################################################################
# script to fetch commodity prices from imf's api
# initial date: 08/09/2016
######################################################################
import imf
import pandas as pd

df = imf.fetch_imf("COMMP")
df.to_csv("../commodity_imf.csv", header=True, index=True)
