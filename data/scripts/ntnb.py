######################################################################
# script to fetch information on ntn-b from Brazilian Treasry
# initial date: 04/09/2016
######################################################################
import pandas as pd

url = "http://sisweb.tesouro.gov.br/apex/COSIS_SISTD.obtem_arquivo?p_id=251:82537"

df = pd.read_excel(url, 2, skiprows = [0, 1], index_col = 0,
                   names = ["Bid yield", "Offer yield",
                            "Bid price", "Offer Price", "Base price"])
df.index.name = "date"
df.to_csv("../ntnb.csv", header=True, index=True)
