######################################################################
# Script to download data for monetary policy map
# initial date: 30/06/2016
######################################################################
from bcb import *
import json, os
import pandas as pd
import numpy as np
from datetime import datetime

series = {"433": "ipca", "4466": "core", "13521": "target"}
today = datetime.today().strftime("%d/%m/%Y")


df_ipca = fetch_bcb(["433", "4466"], "01/01/1993",today)
df_target = fetch_bcb(["13521"], "01/01/1993",today)
df = pd.merge(df_ipca, df_target, left_index=True,
                  right_index=True, how="outer").fillna(method="pad")
df.columns = [series[s] for s in df.columns]



# series manipulations
df_inf = df[['ipca', 'core']].dropna()
df_inf12 = ((1+df_inf/100).cumprod().pct_change(periods=12)*100).dropna()

# target

df['upper'] = df['target'] +2.0
df['lower'] = df['target'] - 2.0

# final
start_date = "2000-01-01"
df_final = pd.merge(df_inf12, df[['target', 'upper', 'lower']].dropna(),
                    left_index=True, right_index=True, how='inner')
df_f = df_final[start_date:]
df_f.to_csv('../mom_policy_map.csv', header=True, index=True)
