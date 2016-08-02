######################################################################
# fetch data on BRL from BCB webserive
#
######################################################################

from bcb import *
from datetime import datetime


date_ini = "01/01/2010"
today = datetime.today().strftime("%d/%m/%Y")

series = {"001": "BRLUSD"}

df = fetch_bcb(series.keys(), date_ini, today)

df.columns = ["BRLUSD"]

df.to_csv("../brlusd.csv", header=True, index=True)
