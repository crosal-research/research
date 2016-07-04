######################################################################
# script to fetch data about terms of trade for Brazil
# initial date: 04/07/2016
######################################################################
import finnacloud_api as fa
import json, os
import pandas as pd


## finnacloud bloiler place
f_dir = os.path.join(os.path.expanduser('~'),"crosal/.finnacloud.json")
key = json.loads(open(f_dir).read())['key'].encode('utf-8')
fc = fa.Finn_Api(key)


## fetch data
series = ['bcb.brexvolt', 'BCB.BRIMPVOLT', 'BCB.BREXPTM', 'BCB.BRIMPTM']
df = fc.get_series(series).dropna()
df.to_csv('../terms_of_trade.csv', index=True, header=True)
