######################################################################
# script to fetch currency data from the Bank of England
# inital date: 17/07/2016
######################################################################
import pandas as pd
from datetime import datetime


__all__ = ['fetch_boe']

def _build_url(tickers, date_ini, date_final):
    tcks = (",").join(tickers)
    # _url = "http://www.bankofengland.co.uk:10065/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&" \
    #        "Datefrom={}&Dateto={}&SeriesCodes={}&CSVF=CN&UsingCodes=" \
    #        "Y&VPD=Y&VFD=N".format(date_ini, date_final, tcks)

    _url = "http://www.bankofengland.co.uk:10065/boeapps/iadb/fromshowcolumns.asp?csv.x=yes&Datefrom=01/Feb/2006&Dateto=01/Oct/2007 &SeriesCodes=LPMAUZI,LPMAVAA&CSVF=TN&UsingCodes=Y&VPD"
    return _url


def fetch_boe(tickers, date_ini, date_final):
    url = _build_url(tickers, date_ini, date_final)
    df = pd.read_csv(url)
    return df



series = {"XUDLB8KL": "Brazilian Real", "XUDLADD": "australian dollar",
          "XUDLERD": "Euro", "XUDLCDD": "canadian dollar", "XUDLBK73": "chiniese yuan",
          "XUDLBK75": "Turkish Lira", "XUDLBK64": "Indian Rupee"}


date_ini = "01/Feb/2016"
date_final = "14/Feb/2016"
