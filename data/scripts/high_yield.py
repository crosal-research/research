######################################################################
# script to retrieve high yield spreads from fred's api
# initial date: 13/07/2016
######################################################################
from fred import *
import pandas as pd
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

series = {"BAMLH0A0HYM2":"BofA US High Yield Spreads", "BAMLEMHBHYCRPIOAS": "BofA EMs High Yield Corporate Spreads",
          "BAMLEMIBHGCRPIOAS": "BofA EMs High Grade Corporate Spreads", "BAMLC0A1CAAA": "BofA US AAA Spreads"}


df = fetch_fred(series.keys())
df.columns = [series[d] for d in df.columns]
df.to_csv(os.path.join(caminho, "high_yields.csv"), header=True, index_col=True)
