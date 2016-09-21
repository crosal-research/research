######################################################################
# fetch data on BRL from BCB webserive
#
######################################################################
from bcb import *
from datetime import datetime
import os


#
caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

date_ini = "01/01/2003"
today = datetime.today().strftime("%d/%m/%Y")

series = {"001": "BRLUSD"}

df = fetch_bcb(series.keys(), date_ini, today)

df.columns = ["BRLUSD"]

df.to_csv(os.path.join(caminho, "brlusd.csv"), header=True, index=True)
