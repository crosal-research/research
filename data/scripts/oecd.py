######################################################################
# retrieves data from oecd api
# initial date: 21/07/2016
# comment: still very incomplete. tested only for ids QNA and MEI
######################################################################

import pandas as pd
import requests
import json
import xmltodict
import collections

__all__ = ["fetch_oecd_dbs", "fetch_oecd_dimensions", "fetch_oecd_codes",
           "fetch_oecd"]


_url_data = "http://stats.oecd.org/SDMX-JSON/data/"
_url_structure = "http://stats.oecd.org/restsdmx/sdmx.ashx/GetDataStructure/"


def fetch_oecd_dbs():
    '''
    return a data frame with codes and mames of all databases of oecd.
    output:
    data frame: index - id, columns = ["Name"]
    '''
    url = _url_structure+"All"
    root = xmltodict.parse(requests.get(url).text.encode("utf-8"))
    doc = root["message:Structure"]["message:KeyFamilies"]["KeyFamily"]
    return pd.DataFrame([(d["@id"], d["Name"][0]["#text"]) for d in doc],
                        columns=["id", "Name"]).set_index("id")


def fetch_oecd_codes(id, dimension):
    '''
    takes database id and dimension as input and returns a dataframe with dbs' dimensions.
    -input:
    string - db's id.
    -output:
    pandas dataframe
    '''
    url = _url_structure+"{}".format(id)
    root = xmltodict.parse(requests.get(url).text.encode("utf-8"))
    doc = root["message:Structure"]["message:CodeLists"]["CodeList"]
    codes = [d for d in doc if d["@id"]==dimension][0]["Code"]
    return pd.DataFrame([(c['@value'], c['Description'][0]["#text"]) for c in codes],
                        columns=["codes", "location"]).set_index("codes")


def fetch_oecd_dimensions(id):
    '''
    takes database id as input and returns a dataframe with dbs' dimensions.
    -input:
    string - db's id.
    -output:
    pandas dataframe
    '''
    url = _url_structure+"{}".format(id)
    doc = xmltodict.parse(requests.get(url).text.encode("utf-8"))
    doc_new = doc["message:Structure"]["message:KeyFamilies"]["KeyFamily"] \
        ["Components"]["Dimension"]
    return pd.DataFrame([(d['@conceptRef'], d['@codelist']) for d in doc_new],
                        columns=["reference", "code"]).set_index("reference")


def _parse_data(data):
    return []


def fetch_oecd(id, agency="all", **p):
    '''
    takes bd id, params and agency as inputs and returns dataframe with
    obsvation of series.
    input:
    - id: string - db's code
    - params: OrderedDict - parameter of the rest url
    - agency: string - agency where the data is from.
    '''
    params = collections.OrderedDict()
    params["locations"] = p['locations']
    params["series"] = p['series']
    params["var"] = p['var']
    params["freq"] = p["freq"]

    par = ".".join(["+".join(params[k]) for k in params])
    url = _url_data+"{}/{}/{}?".format(id, par, agency)
    return url
#    return requests.get(url).text.encode("utf-8")
