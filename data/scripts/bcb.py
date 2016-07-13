######################################################################
# script to download data from BCB's webservice
# initial date: 13/07/2016
######################################################################
import suds.client
import suds_requests
import pandas as pd

__all__ = ['fetch_bcb']


url = "https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl"

c = suds.client.Client(url, transport=suds_requests.RequestsTransport())


def _parse_resp(resp):
    """
    takes a list, a response to a webservice resquest, and parses it. Returns
    a pandas data frame
    input:
    -----
    - resp: list
    ouput:
    -----
    - pandas data frame
    """
    vals = []
    for obs in resp.valores:
        dat = pd.datetime(obs.ano, obs.mes, obs.dia)
        val = obs.valor if obs.valor is not None else "NaN"
        vals.append([dat, val])
    df = pd.DataFrame(vals).set_index(0)
    df.columns = [resp.oid]
    return df


def fetch_bcb(series, date_ini='01/01/2016', date_final='31/01/2016'):
    """
    takes a list of BCB's sereusm abd begining and ending date. Returns
    a pandas data frame
    input:
    -----
    - resp: list of ticker of series.
    - date_ini = string.
    - date_final = string.
    ouput:
    -----
    - pandas data frame
    """
    resp = c.service.getValoresSeriesVO(series, date_ini, date_final)
    df = _parse_resp(resp[0])
    for s in resp[1:]:
        df = pd.merge(df, _parse_resp(s), left_index=True,
                      right_index=True, how="outer")
    df.index.name = "date"
    return df
