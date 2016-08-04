######################################################################
# script to download data from fred
# initial date: 07/07/2016
# comment: need to optimise to single requests session.
######################################################################
import requests
import pandas as pd
import json

__all__ = ["fetch_fred"]

_f_dir = "/home/jmrosal/Documents/crosal/.keys.json"
_key = json.loads(open(_f_dir).read())['fred']['key'].encode('utf-8')


def _parse_data(fred_resp, ticker):
    '''
    parses single series from a response from fred's api and return data frame.
    input:
    -fred_resp: string - text to be parsed
    output: dataframe
    '''
    resp = json.loads(fred_resp)
    data = [[s['date'], s['value']] for s in resp['observations']]
    return pd.DataFrame(data, columns=["date", ticker]).set_index('date')


def fetch_fred(tickers):
    '''
    fetch multple series from fred api and return data frame
    input:
    -tickers: [str], where str are tickers
    output: dataframe.
    '''
    s = requests.session()
    address = "https://api.stlouisfed.org/fred/series/observations?" \
              "series_id={}&api_key={}&file_type=json"
    url = address.format(tickers[0], _key)
    df = _parse_data(s.get(url).text, tickers[0])
    for tkc in tickers[1:]:
        url = address.format(tkc, _key)
        df = pd.merge(df, _parse_data(s.get(url).text, tkc), right_index=True,
                      left_index=True, how="outer")
    s.close()
    return df
