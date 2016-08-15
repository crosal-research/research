######################################################################
# fetch data on US CPI from Fred's API
# initial date: 15/08/2016
######################################################################
import fred

series = ["CPIAUCSL", "CPILFESL"]

df = fred.fetch_fred(series)
df.to_csv("../cpi_us.csv", header=True, index=True)
