# coding: utf-8

######################################################################
# script to download data on service
# initial date: 06/07/2016
######################################################################
from ibge import *


## categories: no adjusted
url = "http://www.sidra.ibge.gov.br/api/values/t/3840" + \
      "/p/all/v/3801/c12355/{}/n1/1/f/a"

## categories: sa adjusted
url_sa = "http://www.sidra.ibge.gov.br/api/values/t/3840" + \
      "/p/all/v/6945/c12355/{}/n1/1/f/a"


d = {"107071":  "Total",
"106869":  "Servicos prestados as familias",
"106870":  "Servicos de alojamento e alimentacao",
"31396":   "Outros servicos prestados as familias",
"106874":  "Servicos de informacao e comunicacao",
"31397":   "Servicos de Tecnologia de Informacao e Comunicacao",
"39321":   "Telecomunicacoes",
"39322":   "Servicos de Tecnologia da Informacao",
"31398":   "Servicos audiovisuais, de edicao e agencias de noticias",
"31399":   "profissionais, administrativos e complementares",
"31400":   "Servicos tecnico-profissionais",
"31421":   "Servicos administrativos e complementares",
"106876":  "servicos auxiliares aos transportes e correio",
"31422":   "Transporte terrestre",
"31423":   "Transporte aquaviario",
"31424":   "Transporte aereo",
"31425":   "Armazenagem, servicos auxiliares aos transportes e correio",
"31426":    "Outros servicos"}

series = d.keys()
names = [d[s] for s in series]

urls = [url.format(s) for s in series]
url_sa = [url_sa.format(s) for s in series]
df = ibge_fetch(urls)
df_sa = ibge_fetch(url_sa)
df.columns = [d[k] for k in df.columns]
df_sa.columns = [d[k] for k in df_sa.columns]
df.index.name = "Date"
df_sa.index.name = "Date"

df.to_csv("../servicos_brazil.csv")
df_sa.to_csv("../servicos_brazil_sa.csv")
