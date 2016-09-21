######################################################################
# script to calculate core measures from raw data
# initial date: 19/08/2016
######################################################################
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import json

df = pd.read_csv("../data/ipca.csv", index_col=[0,1])

# fetch groups
d = json.load(open("../data/scripts/ipca/indexes.json"))
groups = [int(i) for i in d if len(d[i].split(".")[0]) == 4]
names = [d[i].split(".")[1] for i in d if len(d[i].split(".")[0]) <= 4]


df = pd.read_csv("../data/ipca.csv", index_col=[0,1])


# calculates monthly ipca
def ipca(df, date, d):
    '''
    Calculate ipca from raw data
    Inputs:
    - df: pandas data frame with raw data
    - date: string - format: %Y-%m-%d")
    - d: dict (indexes of the raw data)
    '''
    # items for the ipca
    gr = [int(i) for i in d if len(d[i].split(".")[0]) == 4]
    return (df['mom'][date].loc[gr].dot(df['peso'][date].loc[gr]))/100


# calculates
def exclusao(df, date, d):
    '''
    Calculate ex-core from raw data
    Inputs:
    - df: pandas data frame with raw data
    - date: string - format: %Y-%m-%d")
    - d: dict (indexes of the raw data)
    '''
