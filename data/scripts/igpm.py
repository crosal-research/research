######################################################################
# fetch data on igpdi from bcb's webservice
# initial date: 18/08/2016
######################################################################
from bcb import fetch_bcb
from datetime import datetime
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

series = {'190': "IGP",
          '225':"IPA",
          '191': "IPC",
          '192': "INCC",
          '7459': "IPAIND",
          '7460': "IPAG"}


date_ini = '01/01/1995'
today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), date_ini, today)
df.columns = [series[d] for d in df.columns]
df.to_csv(os.path.join(caminho, "igpdi.csv"), header=True, index=True)
