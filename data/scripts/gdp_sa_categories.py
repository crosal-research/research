######################################################################
# Script to fetch gdp data fro ibge sidra api
# initial date:
# comment: fix the data to quarterly from monthly.
######################################################################
from ibge import *


## Data to fetch gdp by categories
url = "http://www.sidra.ibge.gov.br/api/values/t/1621" + \
      "/p/all/v/584/c11255/{}/n1/1/f/a"

d= {"90687":  "Agropecuaria - total",
    "90691":  "Industria - total",
    "90692":  "Extrativa mineral",
    "90693":  "Transformacao",
    "90695":  "Producao e distribuicao de eletricidade, gas, agua, esgoto e limpeza urbana",
    "90694":  "Construcao civil",
    "90696":  "Servicos - total",
    "90697":  "Comercio",
    "90698":  "Transporte, armazenagem e correio",
    "90699":  "Servicos de informacao",
    "90700":  "Intermediacao financeira, seguros, previdencia complementar e servicos relacionados",
    "90702":  "Atividades imobiliarias",
    "90701":  "Outros servicos",
    "90703":  "Administracao, saude e educacao publicas e seguridade social",
    "90705":  "Valor adicionado a precos basicos",
    "90707":  "PIB a precos de mercado",
    "93404":  "Despesa de consumo das familias",
    "93405":  "Despesa de consumo da administracao publica",
    "93406":  "Formacao bruta de capital fixo",
    "93407":  "Exportacao de bens e servicos",
    "93408":  "Importacao de bens e servicos (-)"}

series = d.keys()
names = [d[k] for k in series]
urls = [url.format(s) for s in series]


## fetch data
df = ibge_fetch(urls, freq="Q")
df.columns = names
df.index.name = "Date"
df.to_csv("../gdp_sa_categories.csv")
