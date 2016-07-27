######################################################################
# retrieve data on central government fiscal accounts for BZ
# initial date: 27/07/2016
######################################################################
from bcb import *
from datetime import datetime

series = {"7544": "Total_rev",
          "7545": "total_rev_treasury",
          "7546": "total_rev_ss",
          "7547": "total_outlays",
          "7548": "total_outlays_treasury",
          "7549": "transfers_to_others",
          "7550": "total_outlays_treasury_recor",
          "7551": "trans_treasury_to_bcb",
          "7552": "outlays_ss",
          "7553": "outlays_civil_servants",
          "7554": "primary_resul_treasury",
          "7555": "primary_result_ss",
          "7556": "primary_result_bcb",
          "7557": "primary_result_total",
          "7556": "errors",
          "24389": "outlays_compulsory",
          "24390": "outlays_discricionary",
          "24391": "revenues_by_RFB",
          "24392": "revenues_not_RFB",
          "24393": "incentives",
          "24394": "net_revenues"}

date_ini = "31/01/1997"
today = datetime.today().strftime("%d/%m/%Y")

df = fetch_bcb(series.keys(), date_ini, today)
df.columns = [series[d] for d in df.columns]
df.to_csv("../central_gov_bz.csv", head=True, index=True)
