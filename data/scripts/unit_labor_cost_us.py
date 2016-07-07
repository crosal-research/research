######################################################################
# fetch data for unit labor cost, Brazil
# initial date: 04/07/2016
######################################################################
import finnacloud_api as fa
import json, os
import pandas as pd


f_dir = os.path.join(os.path.expanduser('~'),"crosal/.finnacloud.json")
key = json.loads(open(f_dir).read())['key'].encode('utf-8')
fc = fa.Finn_Api(key)


series = ['FRED.ULCNFB']
df = fc.get_series(series)
df.columns = ["cut"]

# correction on no-existing date
dates = []
for x in df.index:
    if pd.to_datetime(x).month in [1, 4, 7, 10]:
        dates.append(True)
    else:
        dates.append(False)


df_final = df[dates]

# save onto the disk
df_final.to_csv("../cut_us.csv", header=True, index=True)
