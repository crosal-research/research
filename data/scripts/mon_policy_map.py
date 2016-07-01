######################################################################
# Script to download data for monetary policy map
# initial date: 30/06/2016
######################################################################
import finnacloud_api as fa
import json, os
import pandas as pd
import numpy as np

f_dir = os.path.join(os.path.expanduser('~'),"crosal/.finnacloud.json")
key = json.loads(open(f_dir).read())['key'].encode('utf-8')
fc = fa.Finn_Api(key)


series = ["bcb.ipcam", 'BCB.BRIPCACORESMAVEM', 'BCB.BRINFTARGET']
df = fc.get_series(series)
df.columns = ["ipca", 'core', 'target']
df['target'][-1] = 4.5


# series manipulations
df_inf = df[['ipca', 'core']].dropna()
df_inf12 = pd.rolling_apply(df_inf, 12, lambda x: np.prod(1+x/100) -1)*100

# target
df_center = pd.DataFrame(df['target'].fillna(method="pad"))
df_upper = df_center + 2.0
df_lower = df_center - 2.0

df_target = pd.merge(df_center, df_lower, left_index=True, right_index=True, how='inner')
df_target = pd.merge(df_target, df_upper, left_index=True, right_index=True, how='inner').dropna()

# final
start_date = "2000-01-01"
df_final = pd.merge(df_inf12, df_target, left_index=True, right_index=True, how='inner')
df_f = df_final[df_final.index >= start_date]
df_f.to_csv('../mom_poliy_map.csv', header=True, index=True)
