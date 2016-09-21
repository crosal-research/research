######################################################################
# fetch data on US CPI from Fred's API
# initial date: 15/08/2016
######################################################################
import fred
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


series = ["CPIAUCSL", "CPILFESL"]

df = fred.fetch_fred(series)
df.to_csv(os.path.join(caminho, "cpi_us.csv"), header=True, index=True)
