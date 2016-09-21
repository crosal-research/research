######################################################################
# script to retrieve nuci from bcb's website
# initial date: 08/08/2016
######################################################################
import bcb
import os
from datetime import datetime

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series = {"24352": "nuci_total", "13948":"nuci_fiesp"}

date_ini = "01/01/2001"
today = datetime.today().strftime("%d/%m/%Y")

df = bcb.fetch_bcb(series.keys(), date_ini, today)

df.columns = [series[d] for d in df.columns]

df.to_csv(os.path.join(caminho, "nuci_bz.csv"), header=True, index=True)
