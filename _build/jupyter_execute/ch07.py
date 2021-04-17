# Ch7 Excel File Manipulation with pandas

## Case Study: Excel Reporting

import pandas as pd

df = pd.read_excel("sales_data/new/January.xlsx")
df.info()

## Reading Excel Files with pandas

df = pd.read_excel("xl/stores.xlsx",
                   sheet_name="2019", skiprows=1, usecols="B:F")
df

df.info()

def fix_missing(x):
  return False if x in ["", "MISSING"] else x

df = pd.read_excel("xl/stores.xlsx",
                   sheet_name="2019", skiprows=1, usecols="B:F",
                   converters={"Flagship": fix_missing})
df

# The Flagship column now has Dtype "bool"
df.info()

sheets = pd.read_excel("xl/stores.xlsx", sheet_name=["2019", "2020"],
                       skiprows=1, usecols=["Store", "Employees"])
sheets["2019"].head(2)

df = pd.read_excel("xl/stores.xlsx", sheet_name=0,
                   skiprows=2, skipfooter=3,
                   usecols="B:C,F", header=None,
                   names=["Branch", "Employee_Count", "Is_Flagship"])
df

df = pd.read_excel("xl/stores.xlsx", sheet_name="2019",
                   skiprows=1, usecols="B,C,F", skipfooter=2,
                   na_values="MISSING", keep_default_na=False)
df

f = open("output.txt", "w")
f.write("Some text")
f.close()

### Context Managers and the with Statement

with open("output.txt", "w") as f:
  f.write("Some text")

with pd.ExcelFile("xl/stores.xls") as f:
  df1 = pd.read_excel(f, "2019", skiprows=1, usecols="B:F", nrows=2)
  df2 = pd.read_excel(f, "2020", skiprows=1, usecols="B:F", nrows=2)

df1

stores = pd.ExcelFile("xl/stores.xlsx")
stores.sheet_names

url = ("https://raw.githubusercontent.com/fzumstein/"
       "python-for-excel/1st-edition/xl/stores.xlsx")
pd.read_excel(url, skiprows=1, usecols="B:E", nrows=2)

### Writing Excel Files with pandas

import numpy as np
import datetime as dt

data = [[dt.datetime(2020, 1, 1, 10, 13), 2.222, 1, True],
        [dt.datetime(2020, 1, 2), np.nan, 2, False],
        [dt.datetime(2020, 1, 2), np.inf, 3, True]]
df = pd.DataFrame(data=data,
                  columns=["Dates", "Floats", "Integers", "Booleans"])
df.index.name = "index"
df

df.to_excel("written_with_pandas.xlsx", sheet_name="Output",
            startrow=1, startcol=1, index=True, header=True,
            na_rep="<NA>", inf_rep="<INF>")

with pd.ExcelWriter("written_with_pandas2.xlsx") as writer:
  df.to_excel(writer, sheet_name="Sheet1", startrow=1, startcol=1)
  df.to_excel(writer, sheet_name="Sheet1", startrow=10, startcol=1)
  df.to_excel(writer, sheet_name="Sheet2")