######################################################################
# retrieves credit volume data from BCB webservices
# initial date: 14/07/2016
######################################################################p
import pandas as pd
import os
from datetime import datetime
from bcb import *

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"



series = {'20539':"Total", '20540':"Institutions",
          '20541': "Households", '20542':"non-earmarked", '20593':"earmarked",
          '20594':"earmarked_com", '4380':"GDP"}

today = datetime.today().strftime("%d/%m/%Y")
df = fetch_bcb(series.keys(), '01/03/2006', today)


df.columns = [series[s] for s in df.columns]
df.to_csv(os.path.join(caminho, 'credit_volume.csv'), header=True, indexo=True)
