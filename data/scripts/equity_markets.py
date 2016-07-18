######################################################################
# script to fetch equity market prices from yahoo
# initial date: 17/07/2016
######################################################################
from yahoo import *
from datetime import datetime


today = datetime.today().strftime("%m/%d/%Y")

series = ["^BVSP"]


df = fetch_yahoo(series[0], "2011/01/01", today)
