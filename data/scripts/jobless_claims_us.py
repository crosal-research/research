######################################################################
# Script to fetch jobless claims data for the US
# initial date: 28/09/2016
######################################################################
import pandas as pd
import fred
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series =["ICSA", "IC4WSA"]

df = fred.fetch_fred(series)
df.to_csv(os.path.join(caminho, "jobless_claims_us.csv"),
      index=True, header=True)
