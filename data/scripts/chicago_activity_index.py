######################################################################
# fetch the fed chicago actiity index from Fed
# initial date: 03/10/2016
######################################################################
import fred

series = ["CFNAI"]

df = fred.fetch_fred(series)
