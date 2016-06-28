######################################################################
# Chart for interest rates sprads
# initial date: 28/06/2016
######################################################################

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


df = pd.read_csv("../data/interest_spread.csv", header=0, index_col=0)

## chart
