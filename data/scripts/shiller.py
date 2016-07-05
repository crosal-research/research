################################################################################
# script to download and save pe info from shiller
# initial date: 05/07/2016
################################################################################

import pandas as pd

# fetch data
url = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"

df = pd.read_excel(url, sheetname=0, header=0, skiprows=[0, 1, 2, 3, 4, 5, 6],
                   parse_cols=[0, 10], names=["date", "cape"]).dropna()
df.set_index("date", inplace=True)
df.index = pd.date_range("1881-01-01", periods=len(df.index), freq="M")
df.index.name = "date"

# auxiliar data
df.loc[:, "ave"] = pd.DataFrame([df.mean() for i in range(0, len(df.index))], index=df.index)
df.to_csv("../shiller_ave.csv")
