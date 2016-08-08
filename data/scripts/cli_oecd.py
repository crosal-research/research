######################################################################
# script to fetch CLI from oecd's o side
# initial date: 05/08/1970
######################################################################
import oecd

id = "MEI_CLI"

indexes ={"BSCICP03": "Business Confidence Indicator-M",
          "CSCICP03"  "Consumer Confidence Indicator-M"
          "LOLITOAA": "Composite Leading Indicator Amplitude Adjusted - M",
          "LORSGPOR_IXOBSA": "Seasonally Adjusted GDP Index - Q"}


# consumer confidence
df = oecd.fetch_oecd(id, ["GBR", "OECDE"], "CSCICP03")


# business confidence
df = oecd.fetch_oecd(id, ["GBR", "OECDE"], "BSCICP03")
