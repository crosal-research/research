######################################################################
# script to fetch data from BoE's webservices
# initial date: 09/08/2016
# comment: tested only for exchange rate data
######################################################################
import pandas as pd
import xmltodict
import requests
from datetime import datetime

__all__ = ["fetch_boe"]

_url_base = "http://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?" \
            "VFD=N&csv.x=11&csv.y=13"


def _form_date(date_str, fldate):
    '''
    format the date to be used as query paramter, depending whether it is begining
    or final date.
    input:
    - date_str: string. Represent date (format: %d/%m/%Y")

    '''
    date = pd.to_datetime(date_str, dayfirst=True).strftime("%d-%b-%Y").split("-")
    if fldate == 'ini':
        return "FD={}&FM={}&FY={}".format(date[0], date[1], date[2])
    return "TD={}&TM={}&TY={}".format(date[0], date[1], date[2])

def _form_series(codes):
    return "C="+"&C=".join(codes)

def _form_query(codes, date_ini, date_final):
    return "&{}&{}&{}".format(_form_date(date_ini, 'ini'),
                         _form_date(date_final, ""), _form_series(codes))


def fetch_boe(codes, date_ini, final=None):
    if not final:
        date_final = datetime.today().strftime("%d/%m/%Y")
    else:
        date_final = final
    return pd.read_csv(_url_base + _form_query(codes, date_ini, date_final),
                       index_col=[0], parse_dates=[0])
