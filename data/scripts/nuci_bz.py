######################################################################
# script to retrieve nuci from bcb's website
# initial date: 08/08/2016
######################################################################
import bcb
from datetime import datetime

series = {"1344": "nuci_total"}

date_ini = "30/04/1970"
today = datetime.today().strftime("%d/%m/%Y")

df = bcb.fetch_bcb(series.keys(), date_ini, today)
