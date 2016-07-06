###########################################################################
# script to fetch data on brazil's industry by categoria and ativities (sa)
# initial Date: 06/07/2016
###########################################################################
from ibge import *


## atividades
url = "http://www.sidra.ibge.gov.br/api/values/t/3653" + \
      "/p/all/v/3134/c544/{}/n1/1/f/a"

series = ["129314", "129315", "129316", "129317", "129318",
          "129319", "129320", "129321", "129322", "129323",
          "129324", "129325", "129326", "129328", "129329",
          "129330", "129331", "129332", "129333", "129334",
          "129335", "129336", "129337", "129338", "129339",
          "129340", "129341", "129342"]

urls = [url.format(s) for s in series]

df = ibge_fetch(urls)
df.columns = ["Geral", "Extractive", "Transforming", "Food",
              "Beverage", "Tabacco", "Textile", "Apparel",
              "Leather", "Paper", "Wood", "Printing", "Oil Refinery",
              "Cleaning Products", "Chemicals", "Pharma",
              "Rubber", "Mineral (non-metalics)", "Metalurgy",
              "Metallics", "IT", "Eletronics", "Machinery", "Autos",
              "Transportation", "Furniture", "Others", "Maintanance"]
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

series1 = ['129283', '129301', '129300', '129305', '129278']
names1 = [cat[k] for k in series1]

urls1 = [url1.format(s) for s in series1]

df1 = ibge_fetch(urls1)
df1.columns = names1
df1.index.name1 = "Date"

df1.to_csv("../ind_categories_sa.csv")
