######################################################################
# script to retrieve data from yahoo finance
# initial data: 16/07/2016
######################################################################
import pandas as pd

__all__ = ["fetch_yahoo"]

def fetch_yahoo(tickers, date_ini, date_final):
    '''
    retrieves data from yahoo finance. Return data frame with date and closing adj price
    inputs:
    - tickers: [string] - yahoo' tickers
    - date_ini: string - initial date (format - ex: 2016/07/01)
    - date_final: string - final date (format - same as above)
    output:
    - pandas data frame
    '''
    url = _build_url(tickers[0], date_ini, date_final)
    df =  pd.read_csv(url, index_col=0, usecols=[0, 6], skiprows=[0],
                       names = ["Date", tickers[0]]).sort_index(ascending=True)
    for t in tickers[1:]:
        url = _build_url(t, date_ini, date_final)
        df = pd.merge(df,
                   pd.read_csv(url, index_col=0, usecols=[0,6], skiprows=[0],
                               names = ["Date", t]).sort_index(ascending=True),
                   left_index=True, right_index=True, how="outer")
    df.columns = tickers
    return df


def _build_url(ticker, date_ini, date_final):
    '''
    function to form url.
    input:
    - ticker: string - asset ticker
    - date_ini: initial date - format: m/d/Y
    - date_final: final date - format: m/d/Y
    output:
    - string - valid yahoo's url
    '''
    d_ini = date_ini.split("/")
    d_final = date_final.split("/")
    dates = "a={}&b={}&c={}&d={}&e={}&f={}&g=d&i" \
            "gnore=.csv".format(str(int(d_ini[0])-1), str(int(d_ini[1])), d_ini[2],
                                str(int(d_final[0])-1), str(int(d_final[1])), d_final[2])
    return "http://chart.finance.yahoo.com/table.csv?s={}&{}".format(ticker, dates)
