######################################################################
# Script to download from finnacloud interest rate spread.
# Initial date: 28/06/2016
######################################################################
import finnacloud_api as fa
import json, os

f_dir = os.path.join(os.path.expanduser('~'),"crosal/.finnacloud.json")
key = json.loads(open(f_dir).read())['key'].encode('utf-8')
fc = fa.Finn_Api(key)
