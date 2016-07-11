######################################################################
# script to draw retail sales for Brazil
# initial date: 11/07/2016
######################################################################p
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# fetch data
df = pd.read_csv("../data/retail_activities_sa.csv", index_col=[0], header=[0])
