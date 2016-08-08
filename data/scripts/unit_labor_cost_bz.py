######################################################################
# fetch data for unit labor cost, Brazil
# initial date: 04/07/2016
######################################################################
import pandas as pd
import bcb
from datetime import datetime


date_ini = "01/01/1990"
today = datetime.today().strftime("%d/%m/%Y")

series = {'11774':"Labor Productivty in USD",'11777':"Deflated Wage cost in USD"}
df = bcb.fetch_bcb(series.keys(), date_ini, today)
df.columns = [series[d] for d in df.columns]
df.to_csv("../cut.csv", header=True, index=True)
