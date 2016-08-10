######################################################################
# script to fetch data from BoE's webservices
# initial date: 09/08/2016
# comment: tested only for exchange rate data
#####################################################################
import boe
import pandas as pd
from datetime import datetime


## Boe Info
series = {"EC8":
          {"name": 'Australian Dollar' ,
           "ticker":"XUDLADD"},
          "RLT":
          {"name": "Brazilian Real",
           "ticker":"XUDLB8KL"},
          "IIK":
          {"name": "Indian Ruppee",
           "ticker": "XUDLBK64"},
          "IIL":
          {"name": "Israeli Shekel",
           "ticker":"XUDLBK65"},
          "IIM":
          {"name": "Malaysian Ringgit",
           "ticker":"XUDLBK66"},
          "IIO":
          {"name": "Russian Ruble",
           "ticker": "XUDLBK69"},
          "IIP":
          {"name": "Thai Bath",
           "ticker":"XUDLBK72"},
          "IIQ":
          {"name": "Chinese Yuan",
           "ticker": "XUDLBK73"},
          "IIR":
          {"name":"South Korean Won",
           "ticker":"XUDLBK74"},
          "IIS":
          {"name": "Turkish Lira",
           "ticker":"XUDLBK75"},
          "ECV":
          {"name":"Canadian Dollar",
           "ticker":"XUDLCDD"},
          "C8H":
          {"name":"Euro",
           "ticker": "XUDLERD"},
          "ECW":
          {"name": "Sterling",
           "ticker": "XUDLGBD"},
          "EC4":
          {"name": "Danish Krona",
           "ticker": "XUDLDKD"},
          "ECI":
          {"name": "Hong Kong Dollar",
           "ticker": "XUDLHDD"},
          "C8L":
          {"name": "Yen",
           "ticker": "XUDLJYD"},
          "EC5":
          {"name": "New Zealand Dollar",
           "ticker": "XUDLNDD"},
          "ECJ":
          {"name": "Swiss Franc" ,
           "ticker": "XUDLSFD"},
          "ECY":
          {"name": "Swedish Krona",
           "ticker": "XUDLSKD"
          },
          "EC7":
          {"name": "Singapure Dollar",
           "ticker": "XUDLSGD"},
          "ECR":
          {"name": "Saudi Riyal",
           "ticker": "XUDLSRD"},
          "ECS":
          {"name": "Taiwan Dollar",
           "ticker": "XUDLTWD"},
          "ECT":
          {"name": "South African Rand",
           "ticker":"XUDLZRD"}}


df = boe.fetch_boe(["RLT", "ECT", "EC5", "IIK", "ECV", "IIO"], "01/01/2016")
df.columns = [series[s]["name"] for d in df.columns for s in series if series[s]["ticker"] == d]
