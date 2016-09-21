# coding: utf-8

# #####################################################################
# script to fetch data from sidra's api on retail (sa data)
# initial date: 06/07/2016
######################################################################
from ibge import *
import pandas as pd
import os

caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


## atividades
url = "http://www.sidra.ibge.gov.br/api/values/t/3418" + \
      "/p/all/v/564/c11046/12825/c85/{}/n1/1/f/a"

d = {"90671": "Combustíveis e lubrificantes",
     "90672":  "Hipermercados, supermercados, produtos alimentícios, bebidas e fumo",
     "103154":  "Hipermercados e supermercados",
     "90673":  "Tecidos, vestuário e calcados",
     "2759":  "Móveis e eletrodomesticos",
     "103155":  "Artigos farmaceuticos, medicos, ortopedicos, de perfumaria e cosmeticos",
     "103156":  "Livros, jornais, revistas e papelaria",
     "103157":  "Equipamentos e materiais para escritório, informática e comunicacao",
     "103158":  "Outros artigos de uso pessoal e domestico"}

series = d.keys()
names = [d[k] for k in series]
urls = [url.format(s) for s in series]

df = ibge_fetch(urls)
df.columns = names
df.index.name = "Date"


## total, others and contruction
url1 = "http://www.sidra.ibge.gov.br/api/values/t/3416" + \
       "/p/all/v/564/c11046/12825/n1/1/f/a"
url2 = "http://www.sidra.ibge.gov.br/api/values/t/3420" + \
       "/p/all/v/568/c11046/12825/n1/1/f/a"
url3 = "http://www.sidra.ibge.gov.br/api/values/t/3415" + \
       "/p/all/v/1195/c11046/12825/n1/1/f/a"

urls1 = [url1, url2, url3]
names = ["Total", "Auto and Motorbikes", "Construction"]

df1 = ibge_fetch(urls1)
df1.columns = names
df1.index.name = "Date"

## Data Consolidation and save onto to the disk
df_final = pd.merge(df, df1, left_index=True, right_index=True, how="outer")
df_final.to_csv(os.path.join(caminho,"retail_activities_sa.csv"), index=[0], header=True)
