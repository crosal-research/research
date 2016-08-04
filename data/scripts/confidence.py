# coding: utf-8

######################################################################
# script para baixar dados de confiança do site finnacloud
# date: 15/06/2016
######################################################################
import finnacloud_api as fa
import json, os
import pandas as pd


## finnacloud bloiler place
_f_dir = "/home/jmrosal/Documents/crosal/.keys.json"
key = json.loads(open(_f_dir).read())['finnacloud']['key'].encode('utf-8')
fc = fa.Finn_Api(key)


## fetch data

series = ["bcb.bricssafgv", 'bcb.bricc']
df = fc.get_series(series)
df.to_csv("../confianca.csv")
