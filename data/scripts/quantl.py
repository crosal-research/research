######################################################################
# script to download data from quantl's webservice
# initial date: 13/07/2016
######################################################################
import pandas as pd
import numpy as np
import json

__all__ = ['fetch_quantl_ts']


_url_quantl = "https://www.quandl.com/api/v3/datasets//{}/{}.csv?api_key={}&order=asc"


def fetch_quantl_ts(db, series, key):
    """
    Takes a list of quantl's series. Returns
    a pandas data frame
    input:
    -----
    - db: string - quantl database
    - series: [string] - series tickers
    ouput:
    -----
    - pandas data frame
    """
    url = _url_quantl.format(db, series[0], key)
    df = pd.read_csv(url, index_col=[0])
    return df
