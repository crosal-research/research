# coding: utf-8

######################################################################
# script to provide functions to download data from IBGE
# initial date: 06/07/2016
######################################################################

import pandas as pd
import requests


def _fetch_data(reps):
    '''
    function to parse a response from a single series from the ibge API to
    a pandas dataframe. Take a json string and return pandas dataframe.
    inputs:
    - resp: string json
    return: pandas dataframe
    '''
    df = pd.read_json(reps).iloc[1:].pivot("D1C", "D3C", "V")
    dates = pd.to_datetime([d+"01" for d in df.index])
    return pd.DataFrame(df.values, columns=df.columns, index=dates)


def ibge_fetch(urls):
    '''function to fetch series IBGE's api using full url as input. Takes
    a string and returns a pandas dataframe.  -
    urls: list(str) with url.
    return: pandas dataframe
    '''
    s = requests.session()
    df = _fetch_data(s.get(urls[0]).text)
    df.index.name = "date"
    df.columns.name = None

    for url in urls[1:]:
        df_new = _fetch_data(s.get(url).text)
        df_new.index.name = "date"
        df_new.columns.name = None
        df = pd.merge(df, df_new, left_index=True,
                      right_index=True, how="outer")
    s.close()
    return df
