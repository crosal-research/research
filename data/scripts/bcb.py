######################################################################
# script to download data from BCB's webservice
# initial date: 13/07/2016
######################################################################
import suds.client
import suds_requests
import pandas as pd

__all__ = ['fetch_bcb']


url = "https://www3.bcb.gov.br/sgspub/JSP/sgsgeral/FachadaWSSGS.wsdl"

c = suds.client.Client( url, transport=suds_requests.RequestsTransport())


def _parse_resp(resp):
    vals = []
    for obs in resp.valores:
        dat = pd.datetime(obs.ano, obs.mes, obs.dia)
        val = obs.valor if obs.valor is not None else "NaN"
        vals.append([dat, val])
    return pd.DataFrame(vals).set_index(0)


def fetch_bcb(series, date_ini, date_final):
    resp = c.service.getValoresSeriesVO(series, date_ini, date_final)
    df =  _parse_resp(resp[0])
    for s in resp[1:]:
        df = pd.merge(df, _parse_resp(s), left_index=True,
                      right_index=True, how="outer")
    df.index.name = "date"
    df.columns = series
    return df
