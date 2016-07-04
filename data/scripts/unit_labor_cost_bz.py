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


series = ['BCB.BRULTUS']
df = fc.get_series(series)
df.columns = ["cut"]
df.to_csv("../cut.csv", header=True, index=True)
