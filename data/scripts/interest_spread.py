######################################################################
# Script to download from finnacloud interest rate spread.
# Initial date: 28/06/2016
######################################################################
import finnacloud_api as fa
import json, os
import pandas as pd

f_dir = os.path.join(os.path.expanduser('~'),"crosal/.finnacloud.json")
key = json.loads(open(f_dir).read())['key'].encode('utf-8')
fc = fa.Finn_Api(key)

series = ['bcb.selic', 'bcb.cdi6m','bcb.cdi1y']
df = fc.get_series(series)
df.to_csv('./interest_spread.csv', header=True, index=True)
