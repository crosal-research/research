######################################################################
# script to fetch commodity prices from imf's api
# initial date: 08/09/2016
######################################################################
import imf
import os
import pandas as pd

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

df = imf.fetch_imf("COMMP")
df.to_csv(os.path.join(caminho, "commodity_imf.csv"), header=True, index=True)
