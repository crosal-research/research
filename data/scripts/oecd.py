######################################################################
# retrieves data from oecd api
# initial date: 21/07/2016
# comment: totalmente incompleto.
######################################################################

import pandas as pd
import requests
import json
import xml.etree.ElementTree as ET

__all__ = ["fetch_oecd_dbs", "fetch_oecd_struct", "fetch_oecd_codes", "fetch_oecd"]


_url_data = "http://stats.oecd.org/SDMX-JSON/data/"
_url_structure = "http://stats.oecd.org/restsdmx/sdmx.ashx/GetDataStructure/"


def fetch_oecd_struct(id):
    '''
    takes database id as input and returns a dataframe with dbs' dimensions.
    -input:
    string - db's id.
    -output:
    pandas dataframe
    '''
    url = _url_structure+"{}".format(id)
    root = ET.fromstring(requests.get(url).text.encode("utf-8"))
    return root
