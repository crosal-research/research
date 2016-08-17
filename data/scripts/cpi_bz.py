######################################################################
# script to fetch cpi data from bz from ibge's api
# initial date: 18/08/2016
######################################################################
from ibge import ibge_fetch

url_ch = "http://www.sidra.ibge.gov.br/api/values/t/1419/p/last/v/63/c315/all/n1/1/f/a"
url_weight = "http://www.sidra.ibge.gov.br/api/values/t/1419/p/last/v/66/c315/all/n1/1/f/a"


# fetch monthly changes
df = ibge_fetch([url_ch])
df_ch = pd.DataFrame(df.stack())
df_ch.index.names = ["date", "items"]

# fetch month weigth
df1 = ibge_fetch([url_weight])
df1_weight = pd.DataFrame(df1.stack())
df1_weight.index.names = ['date', 'items']

# produces final dataset
df_final = pd.merge(df_ch, df1_weight,
                    right_index=True,
                    left_index=True, how = 'outer')
df_final.columns = ["mom", "peso"]
