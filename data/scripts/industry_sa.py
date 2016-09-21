###########################################################################
# script to fetch data on brazil's industry by categoria and ativities (sa)
# initial Date: 06/07/2016
###########################################################################
from ibge import *
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"

## atividades
url = "http://www.sidra.ibge.gov.br/api/values/t/3653" + \
      "/p/all/v/3134/c544/{}/n1/1/f/a"

series = {"129314": "Geral",
          "129315":"Extractive",
          "129316": "Transforming",
          "129317": "Food",
          "129318": "Beverage",
          "129319": "Tabacco",
          "129320": "Textile",
          "129321": "Apparel",
          "129322": "Leather",
          "129323": "Paper",
          "129324": "Wood",
          "129325": "Printing",
          "129326": "Oil Refinery",
          "129328": "Cleaning Products",
          "129329": "Chemicals",
          "129330": "Pharma",
          "129331": "Rubber",
          "129332": "Mineral (non-metalics)",
          "129333": "Metalurgy",
          "129334": "Metallics",
          "129335": "IT",
          "129336": "Eletronics",
          "129337": "Machinery",
          "129338": "Autos",
          "129339": "Transportation",
          "129340": "Furniture",
          "129341": "Others",
          "129342": "Maintanance"}

urls = [url.format(s) for s in series]

df = ibge_fetch(urls)
df.columns = [series[s] for s in df.columns]
df.index.name = "Date"

df.to_csv("../ind_atividades_sa.csv")


## categories
url1 = "http://www.sidra.ibge.gov.br/api/values/t/3651" + \
       "/p/all/v/3134/c543/{}/n1/1/f/a"

cat = {"129278": "Capital Goods",
       "129283": "Intermediary Goods",
       "129300": "Consumption Goods",
       "129301": "Durable Consumption Goods",
       "129305": "Semi and non-durables"}

names1 = [cat[k] for k in cat]

urls1 = [url1.format(s) for s in cat]

df1 = ibge_fetch(urls1)
df1.columns = [cat[k] for k in df1.columns]
df1.index.name1 = "Date"

df1.to_csv(os.path.join(caminho, "ind_categories_sa.csv"))
