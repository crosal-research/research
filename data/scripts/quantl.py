######################################################################
# script to download data from quantl's webservice
# initial date: 13/07/2016
######################################################################
import pandas as pd


__all__ = ['fetch_quantl_ts']


_url_quantl = "https://www.quandl.com/api/v3/datasets//{}/{}.csv?api_key={}&order=asc&start_date={}&end_date={}"


def fetch_quantl_ts(db, series, key, start='', end=''):
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
    url = _url_quantl.format(db, series[0], key, start, end)
    df = pd.read_csv(url, index_col=[0])
    return df
