######################################################################
# retrieves data from imf api
# initial date: 20/07/2016
# function fetch_imp only tested from COMMP (21/07/2016)
######################################################################

import pandas as pd
import requests
import json


__all__ = ["fetch_imf_dbs", "fetch_imf_struct", "fetch_imf_codes", "fetch_imf"]

_url_data = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/"
_url_structure = "http://dataservices.imf.org/REST/SDMX_JSON.svc/DataStructure/"
_url_flow = "http://dataservices.imf.org/REST/SDMX_JSON.svc/Dataflow/"
_url_codes = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CodeList/"

def fetch_imf_dbs():
    '''
    returns data frame with information on all the dbs provided by the imf api.
    -input:
    -output:
    pandas data frame
    '''
    seriesid = json.loads(requests.get(_url_flow).text) \
               ['Structure']['KeyFamilies']['KeyFamily']
    return pd.DataFrame([([s["@id"], s["Name"]["#text"]]) for s in seriesid],
                        columns = ['id', "Name"]).set_index('id')


def fetch_imf_struct(id):
    '''
    takes database id as input and returns a dataframe with dbs' dimensions.
    -input:
    string - db's id.
    -output:
    pandas dataframe
    '''
    url = _url_structure+"{}".format(id)
    doc_struct = json.loads(requests.get(url).text.encode('utf-8'))['Structure']['KeyFamilies']\
                            ['KeyFamily']['Components']['Dimension']

    return pd.DataFrame([(s['@conceptRef'], s["@codelist"]) for s in doc_struct],
                        columns = ["Concept", "codelist"]).set_index('Concept')


def fetch_imf_codes(code):
    '''
    takes a string indicating the code from db's structure and return all
    codelis related to that code
    '''
    url = _url_codes+"{}".format(code)
    codes = json.loads(requests.get(url).text)["Structure"]["CodeLists"]\
            ["CodeList"]["Code"]
    if type(codes) == type([]):
        return pd.DataFrame([(s["@value"], s["Description"]["#text"]) for s in codes],
                            columns=["Code", "Description"]).set_index("Code")
    else:
        return pd.DataFrame([codes["@value"], codes["Description"]["#text"]],
                             columns = ["Description"])


def _parse_obs(obs):
    '''
    takes a tuple, with 1st item a series string ticker and 2nd array of dictionraries.
    returns a data frame
    input:
    - obs: (string, list(dict))
    output:
    - dataframe: index - dates, columns - values
    '''
    return pd.DataFrame([[pd.to_datetime(v["@TIME_PERIOD"]), float(v["@OBS_VALUE"])]
                         for v in obs[1]],
                        columns=['date', obs[0]]).set_index("date")


def fetch_imf(id, ref_are=[], indicators=[], freq="M"):
    '''
    takes id string representing the db and a default string freq, representing the
    frequency. Returns a dataframe
    input:
    - id: string - db ticker
    - ref_are:list(string) - reference are
    - indicators: list(string) - cl_indicators
    - freq: string - frequency
    output:
    - dataframe: index - date, columns: values for each indicator.
    '''
    labels = {"COMMP":"@COMMODITY"}
    if id in labels:
        url = _url_data+"{}/{}.{}".format(id, "+".join(ref_are), "+".join(indicators))
        series = json.loads(requests.get(url).text)['CompactData']['DataSet']['Series']
        dat = [(s[labels[id]], s['Obs']) for s in series
               if ("Obs" in s.keys() and s["@FREQ"] == freq)]
        df = _parse_obs(dat[0])
        for d in dat[1:]:
            df = pd.merge(df, _parse_obs(d), left_index=True, right_index=True, how="outer")
        return df
    else:
        print "Series not available"
