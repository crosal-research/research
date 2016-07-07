######################################################################
# script to download data from fred
# initial date: 07/07/2016
# comment: need to optimise to single requests session.
######################################################################
import requests
import pandas as pd
import json, os

__all__ = ["fetch_fred"]

_f_dir = os.path.join(os.path.expanduser('~'),"crosal/.fred.json")
_key = json.loads(open(_f_dir).read())['key'].encode('utf-8')


def _fetch_data(ticker):
    '''
    fetch single series from fred and return data frame.
    input:
    -ticker: string - series tickers
    output: dataframe
    '''
    address = "https://api.stlouisfed.org/fred/series/observations?" \
              "series_id={}&api_key={}&file_type=json"
    urls = address.format(ticker, _key)
    resp = json.loads(requests.get(urls).text)
    data = [[s['date'], s['value']] for s in resp['observations']]
    return pd.DataFrame(data, columns=["date", ticker]).set_index('date')


def fetch_fred(tickers):
    '''
    fetch multple series from fred api and return data frame
    input:
    -tickers: [str], where str are tickers
    output: dataframe.
    '''
    if len(tickers) == 1:
        df = _fetch_data(tickers[0])
    else:
        df = _fetch_data(tickers[0])
        for i in tickers[1:]:
            df = pd.merge(df, _fetch_data(i), right_index=True,
                              left_index=True, how="outer")
    return df
