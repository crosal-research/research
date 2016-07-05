######################################################################
# fetch data for effective exchange rate, Brazil
# initial date: 05/07/2016
######################################################################
import finnacloud_api as fa
import json, os
import pandas as pd


f_dir = os.path.join(os.path.expanduser('~'),"crosal/.finnacloud.json")
key = json.loads(open(f_dir).read())['key'].encode('utf-8')
fc = fa.Finn_Api(key)


series = ['BCB.BZFXREAL', 'BCB.BRFXREALPROD']
df = fc.get_series(series)
df.columns = ["fx_real", "fx_prod"]
df.to_csv("../real_fx_rate.csv", header=True, index=True)
