#######################################################################
# Module para baixar dados do FinnaCloud:
# - Classe FcImportError define excecao
# - Class Finn_Api expoe funcionaliadades do cliente
# versao: 0.1
# data: 24/11/2015
######################################################################

import requests
import pandas as pd

key = '94EiufPEcBpsiBgog0Krih9SqMRhSMQ8'


class FcImportError(Exception):
    '''
    Classe que define excecao no caso em que request retorna
    status diferente de 200.
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Finn_Api(object):
    '''
    Class que se inicializa via chave do Api e expoe diferentes
    metodos do API via os metodos de class.
    '''
    def __init__(self, key):
        self.key = key

    def get_key(self):
        '''
        Obtem a chave do api do usuario
        Ouput:
        -----
        - str.
        '''
        return self.key

    def set_key(self, new_key):
        '''
        Imputa a chave do api do usuario na classe
        Input:
        -----
        - new_key: str.
        Ouput:
        -----
        - str.
        '''
        self.key = new_key

    def _try_request(self, request):
        '''
        Checa se request foi bem formulada a partir de um
        objecto request. Se status e 200, retorna seu
        texto; caso contrario, retorna excecao.
        Input:
        -----
        - url: str.
        Ouput:
        -----
        - str ou excecao.
        '''
        if request.ok:
            return request.json()
        else:
            raise FcImportError("Chave de api ou ticker errados")

    def _build_url(self, tickers, start, end):
        '''
        Constroi url para a ser utilizada em request a partir
        do ticker da series, o inicio e o fim das observacoes
        desejadas.
        Input:
        ------
        - ticker: str.
        - start: str.
        - end: str.
        Ouput:
        ------
        - str
        '''
        dom = 'http://www.finnacloud.com/api/' + self.key
        url = '{0}/indicator/{1}/values.json'.format(dom, tickers)
        if start == "" and end == "":
            return url
        elif start != "" and end == "":
            return url + "?startDate={0}&".format(start)
        elif start == "" and end != "":
            return url + "?&endDate={0}".format(end)
        else:
            return url + "?startDate={0}&endDate={1}".format(start, end)

    def get_series(self, tickers, start="", end=""):
        '''
        Faz request na base FinnaCloud para um determinado usuario e
        tickers e returna serie ou tabela.
        Inputs:
        -------
        -ticker: str ou list(str)
        Ouput:
        ------
        - DataFrame (pandas)
        '''
        s = requests.Session()
        if type(tickers) == "".__class__:
            url = self._build_url(tickers, start, end)
            resp = s.get(url)
            df = pd.DataFrame(self._try_request(resp)).set_index('date')
            df.index = pd.to_datetime(df.index, format="%d/%m/%Y")
            df. columns = [tickers]
            df[:] = df.values.astype("float64")
            return df

        if len(tickers) == 1:
            url = self._build_url(tickers[0], start, end)
            resp = s.get(url)
            df = pd.DataFrame(self._try_request(resp)).set_index('date')
            df.index = pd.to_datetime(df.index, format="%d/%m/%Y")
        else:
            url = self._build_url(tickers[0], start, end)
            resp = s.get(url)
            df1 = pd.DataFrame(self._try_request(resp)).set_index('date')
            df1.index = pd.to_datetime(df1.index, format="%d/%m/%Y")
            df = pd.merge(df1, self.get_series(tickers[1:]),
                          left_index=True, right_index=True,
                          how='outer')
        df.columns = tickers
        df[:] = df.values.astype("float")
        s.close()
        return df

    def get_table(self, ticker):
        '''
        Faz request na base FinnaCloud de uma tabela
        a disposicao do usuario
        Inputs:
        ------
        -ticker: str (ticker)
        Ouput:
        ------
        - DataFrame (pandas)
        '''
        domain = 'http://www.finnacloud.com/api'
        url = '{0}/{1}/table/{2}.json'.format(domain, self.key,
                                              ticker)
        resp = requests.get(url)
        df = pd.DataFrame(self._try_request(resp)).set_index('date')
        df.index = pd.to_datetime(df.index, format="%d/%m/%Y")
        df[:] = df.values.astype("float64")
        return df

    def get_meta(self, ticker):
        '''
        Faz request na base FinnaCloud para um determinado usuario e
        ticker e returna informacoes sobre series/ticker
        Inputs:
        -ticker: str (ticker)
        Ouput:
        - DataFrame (pandas)
        '''
        domain = 'http://www.finnacloud.com/api'
        url = '{0}/{1}/indicator/{2}/info.json'.format(domain,
                                                       self.key,
                                                       ticker)
        resp = requests.get(url)
        return pd.DataFrame(self._try_request(resp))

    def get_search(self, words):
        '''
        Faz request para procura na base FinnaCloud para um
        determinado usuario
        e ticker e retorna as series candidatas
        Inputs:
        ------
        -words: list(str)
        Ouput:
        -----
        - DataFrame (pandas)
        '''
        domain = 'http://www.finnacloud.com/api'
        search_words = words if (len(words) <= 1) else "%20".join(words)
        url = '{0}/{1}/search/{2}.json'.format(domain,
                                               self.key, search_words)
        resp = requests.get(url)
        return pd.DataFrame(self._try_request(resp)).set_index("ticker")
