######################################################################
# Script to download data for monetary policy map
# initial date: 30/06/2016
######################################################################
import finnacloud_api as fa
import json, os
import pandas as pd

f_dir = os.path.join(os.path.expanduser('~'),"crosal/.finnacloud.json")
key = json.loads(open(f_dir).read())['key'].encode('utf-8')
fc = fa.Finn_Api(key)
