###################################################################### fetch data on upper and lower house members, Brazil
# initial date: 16/09/2016
######################################################################
import pandas as pd
import os
import suds.client
import suds_requests
import xmltodict


caminho = "/home/jmrosal/Documents/crosal/research/research/data/"


#lower house
url = "http://www.camara.gov.br/SitCamaraWS/Deputados.asmx?wsdl"
c = suds.client.Client(url, transport=suds_requests.RequestsTransport())
resp = c.service.ObterDeputados()

df_dep = pd.DataFrame([dict(d) for d in resp[0]['deputado']])
df = df_dep[['nomeParlamentar', 'partido', 'sexo', 'uf']]

# save
df.to_csv()




# url_lh = "http://www.camara.leg.br/internet/deputado/deputado.xls"
# df_lh = pd.read_excel(url_lh, header=0, parse_cols=[0, 1, 2 , 3])
# df_lh.to_csv(os.path.join(caminho, "lower_house.csv"),
#              header=True, encoding='utf-8')
