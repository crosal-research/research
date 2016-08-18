# coding: utf-8

######################################################################
# fetch data for ipca from sidra ipca
# initial date: 10/07/2016
######################################################################

from ibge import *
import json


d = json.loads(open("./indexes.json", "r").read())

# define items to be downloaded
items = [i for i in d if len(d[i].split(".")[0]) <= 4]
names = [d[i].split(".")[1] for i in d if len(d[i].split(".")[0]) <= 4]
req = ",".join(items)

# prepared urls for requesting mom changes and weights
address_ch = "http://www.sidra.ibge.gov.br/api/values/t/1419" + \
             "/p/all/v/63/c315/{}/n1/1/f/a"
url_ch = address_ch.format(req)

address_weight = "http://www.sidra.ibge.gov.br/api/values/t/1419" + \
                 "/p/all/v/66/c315/{}/n1/1/f/a"
url_weight = address_weight.format(req)

# monthly change
df_ch = ibge_fetch([url_ch])
df_chs = pd.DataFrame(df_ch.stack())
df_chs.index.names = ["date", "items"]

# weights
df_weigth = ibge_fetch([url_weight])
df_weights = pd.DataFrame(df_weigth.stack())
df_weights.index.names = ['date', 'items']

# produces final dataset
df_final = pd.merge(df_chs, df_weights,
                    right_index=True,
                    left_index=True, how = 'outer')
df_final.columns = ["mom", "peso"]


df_final.to_csv("../../data/ipca.csv", head=True, index = True)
