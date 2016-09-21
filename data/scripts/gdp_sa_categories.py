######################################################################
# Script to fetch gdp data fro ibge sidra api
# initial date:
# comment: fix the data to quarterly from monthly.
######################################################################
from ibge import *
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


## Data to fetch gdp by categories
url = "http://www.sidra.ibge.gov.br/api/values/t/1621" + \
      "/p/all/v/584/c11255/{}/n1/1/f/a"

d= {"90687":  "Agriculture",
    "90691":  "Industry - Total",
    "90692":  "Mining",
    "90693":  "Transformation",
    "90695":  "Public Utilities",
    "90694":  "Construction",
    "90696":  "Services - Total",
    "90697":  "Commerce",
    "90698":  "Transport, Storage and Mailing",
    "90699":  "IT",
    "90700":  "Financial Intermediation",
    "90702":  "Real Estate Activity",
    "90701":  "Other Services",
    "90703":  "Public services and Social Security",
    "90705":  "Value Added",
    "90707":  "GDP",
    "93404":  "Household Consumption",
    "93405":  "Public Consumption",
    "93406":  "Net Investment",
    "93407":  "Exports of Goods and Services",
    "93408":  "Imports of Goods and Services"}

series = d.keys()
urls = [url.format(s) for s in series]


## fetch data
df = ibge_fetch(urls, freq="Q")
df.columns = [d[k] for k in df.columns]
df.index.name = "Date"
df.index = pd.date_range(df.index[0], periods = len(df), freq="QS")
df.to_csv(os.path.join(caminho,"gdp_sa_categories.csv"))
