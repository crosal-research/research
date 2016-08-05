######################################################################
# retrieves data from oecd api
# initial date: 21/07/2016
# comment: still very incomplete. tested only for ids: QNA, CLI_MEI
######################################################################

import pandas as pd
import requests
import json
import xmltodict


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
    takes database id and dimension as input and returns a dataframe with dbs' codes.
    -input:
    string - db's id.
    -output:
    pandas dataframe
    '''
    url = _url_structure+"{}".format(id)
    root = xmltodict.parse(requests.get(url).text.encode("utf-8"))
    doc = root["message:Structure"]["message:CodeLists"]["CodeList"]
    codes = [d for d in doc if d["@id"] == dimension][0]["Code"]
    return pd.DataFrame([(c['@value'], c['Description'][0]["#text"]) for c in codes],
                        columns=["codes", dimension]).set_index("codes")


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


def _parse_data(data, location):
    '''
    Parse response of data query. Helper function for oecd_fetch
    input:
    - data: dict
    return:
    - dataframe
    '''
    k = data['dataSets'][0]['series'].keys()[0]
    ds = data['dataSets'][0]['series'][k]['observations']
    #    return pd.DataFrame(data.values())
    dd = [v['id']  for v in data['structure']['dimensions']['observation'][0]['values']]
    dt = pd.to_datetime(dd)
    return pd.DataFrame([v[0] for v in ds.values()],
                        index=dt, columns=[location])



def _url_builder(db_id, location, subject, measure, freq, agency):
    '''
    Builds the right url for data queries. Helper function for
    for fetch_oecd.
    Inputs:
    - db_id: string
    - location: string
    - subject: string
    - measure: string
    - freq: string
    - agency: string
    Output:
    - string
    '''
    if db_id == "QNA":
        params = [location, subject, measure, freq]
    else:
        params = [subject, location, measure, freq]
    par = ".".join(p for p in params if p != "")
    return _url_data+"{}/{}/{}?detail=DataOnly".format(db_id, par, agency)



def fetch_oecd(db_id, location, subject, measure="", freq="M", agency="all"):
    '''
    takes db's id, country, suject of the series, its measure, frequency
    and agency as inputs and returns dataframe with observations of series.
    input:
    - id: string - db's code
    - locations: string      - example: ["GBR", "AUS"]
    - subject: string              - example: "GDP"
    - measure: string              - example: "CUR"
    - freq: string                 - example: "M"
    - agency: string - agency where the data is from.
    output:
    - dataframe
    '''
    s = requests.session()
    url = _url_builder(db_id, location[0], subject, measure, freq, agency)
    df = _parse_data(json.loads(s.get(url).text.encode("utf-8")),
                     location[0])
    for loc in location[1:]:
        url = _url_builder(db_id, loc, subject, measure, freq, agency)
        df_new =  _parse_data(json.loads(s.get(url).text.encode("utf-8")),
                     loc)
        df = pd.merge(df, df_new, left_index=True, right_index=True, how="outer")
    df.index.name = "date"
    s.close()
    return df
