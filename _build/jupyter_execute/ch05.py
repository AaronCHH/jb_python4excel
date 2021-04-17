# Ch05 Data Analysis with pandas

## DataFrame and Series

import pandas as pd

pd.read_excel("xl/course_participants.xlsx")

data=[["Mark", 55, "Italy", 4.5, "Europe"],
      ["John", 33, "USA", 6.7, "America"],
      ["Tim", 41, "USA", 3.9, "America"],
      ["Jenny", 12, "Germany", 9.0, "Europe"]]
df = pd.DataFrame(data=data,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000, 1002, 1003])
df

df.info()

### Index

df.index

df.index.name = "user_id"
df

# "reset_index" turns the index into a column, replacing the
# index with the default index. This corresponds to the DataFrame
# from the beginning that we loaded from Excel.
df.reset_index()

# "reset_index" turns "user_id" into a regular column and
# "set_index" turns the column "name" into the index
df.reset_index().set_index("name")

df.reindex([999, 1000, 1001, 1004])

df.sort_index()

df.sort_values(["continent", "age"])

### Columns

df.columns

df.columns.name = "properties"
df

df.rename(columns={"name": "First Name", "age": "Age"})

df.drop(columns=["name", "country"],
        index=[1000, 1003])

df.T  # Shortcut for df.transpose()

df.loc[:, ["continent", "country", "name", "age", "score"]]

## Data Manipulation

### Selecting Data

# Using scalars for both row and column selection returns a scalar
df.loc[1001, "name"]

# Using a scalar on either the row or column selection returns a Series
df.loc[[1001, 1002], "age"]

# Selecting multiple rows and columns returns a DataFrame
df.loc[:1002, ["name", "country"]]

df.iloc[0, 0]  # Returns a Scalar

df.iloc[[0, 2], 1]  # Returns a Series

df.iloc[:3, [0, 2]]  # Returns a DataFrame

tf = (df["age"] > 40) & (df["country"] == "USA")
tf  # This is a Series with only True/False

df.loc[tf, :]

df.loc[df.index > 1001, :]

df.loc[df["country"].isin(["Italy", "Germany"]), :]

# This could be the yearly rainfall in millimeters
rainfall = pd.DataFrame(data={"City 1": [300.1, 100.2],
                              "City 2": [400.3, 300.4],
                              "City 3": [1000.5, 1100.6]})
rainfall

rainfall < 400

rainfall[rainfall < 400]

# A MultiIndex needs to be sorted
df_multi = df.reset_index().set_index(["continent", "country"])
df_multi = df_multi.sort_index()
df_multi

df_multi.loc["Europe", :]

df_multi.loc[("Europe", "Italy"), :]

df_multi.reset_index(level=0)

### Setting Data

# Copy the DataFrame first to leave the original untouched
df2 = df.copy()

df2.loc[1000, "name"] = "JOHN"
df2

df2.loc[[1000, 1001], "score"] = [3, 4]
df2

tf = (df2["age"] < 20) | (df2["country"] == "USA")
df2.loc[tf, "name"] = "xxx"
df2

# Copy the DataFrame first to leave the original untouched
rainfall2 = rainfall.copy()
rainfall2

# Set the values to 0 wherever they are below 400
rainfall2[rainfall2 < 400] = 0
rainfall2

df2.replace("USA", "U.S.")

df2.loc[:, "discount"] = 0
df2.loc[:, "price"] = [49.9, 49.9, 99.9, 99.9]
df2

df2 = df.copy()  # let's start with a fresh copy
df2.loc[:, "birth year"] = 2021 - df2["age"]
df2

### Missing Data

df2 = df.copy() # let's start with a fresh copy
df2.loc[1000, "score"] = None
df2.loc[1003, :] = None
df2

df2.dropna()

df2.dropna(how="all")

df2.isna()

df2.fillna({"score": df2["score"].mean()})

### Duplicate Data

df.drop_duplicates(["country", "continent"])

df["country"].is_unique

df["country"].unique()

# By default, it marks only duplicates as True, i.e.
# without the first occurrence
df["country"].duplicated()

# To get all rows where "country" is duplicated, use
# keep=False
df.loc[df["country"].duplicated(keep=False), :]

### Arithmetic Operations

rainfall

rainfall + 100

more_rainfall = pd.DataFrame(data=[[100, 200], [300, 400]],
                             index=[1, 2],
                             columns=["City 1", "City 4"])
more_rainfall

rainfall + more_rainfall

rainfall.add(more_rainfall, fill_value=0)

# A Series taken from a row
rainfall.loc[1, :]

rainfall + rainfall.loc[1, :]

# A Series taken from a column
rainfall.loc[:, "City 2"]

rainfall.add(rainfall.loc[:, "City 2"], axis=0)

# Let's create a new DataFrame
users = pd.DataFrame(data=[" mArk ", "JOHN  ", "Tim", " jenny"],
                     columns=["name"])
users

users_cleaned = users.loc[:, "name"].str.strip().str.capitalize()
users_cleaned

users_cleaned.str.startswith("J")

### Applying a Function

rainfall

def format_string(x):
    return f"{x:,.2f}"

# Note that we pass in the function without calling it,
# i.e., format_string and not format_string()!
rainfall.applymap(format_string)

rainfall.applymap(lambda x: f"{x:,.2f}")

## Combining DataFrames

### Concatenating

data=[[15, "France", 4.1, "Becky"],
      [44, "Canada", 6.1, "Leanne"]]
more_users = pd.DataFrame(data=data,
                          columns=["age", "country", "score", "name"],
                          index=[1000, 1011])
more_users

pd.concat([df, more_users], axis=0)

data=[[3, 4],
      [5, 6]]
more_categories = pd.DataFrame(data=data,
                               columns=["quizzes", "logins"],
                               index=[1000, 2000])
more_categories

pd.concat([df, more_categories], axis=1)

### Joining and Merging

df1 = pd.DataFrame(data=[[1, 2], [3, 4], [5, 6]],
                   columns=["A", "B"])
df1

df2 = pd.DataFrame(data=[[10, 20], [30, 40]],
                   columns=["C", "D"], index=[1, 3])
df2

df1.join(df2, how="inner")

df1.join(df2, how="left")

df1.join(df2, how="right")

df1.join(df2, how="outer")

# Add a column called "category" to both DataFrames
df1["category"] = ["a", "b", "c"]
df2["category"] = ["c", "b"]

df1

df2

df1.merge(df2, how="inner", on=["category"])

df1.merge(df2, how="left", on=["category"])

## Data Aggregation and Descriptive Statistics

### Descriptive Statistics

rainfall

rainfall.mean()

rainfall.mean(axis=1)

### Grouping

df.groupby(["continent"]).mean()

df.groupby(["continent", "country"]).mean()

df.groupby(["continent"]).agg(lambda x: x.max() - x.min())

### Pivoting and Melting

data = [["Oranges", "North", 12.30],
        ["Apples", "South", 10.55],
        ["Oranges", "South", 22.00],
        ["Bananas", "South", 5.90],
        ["Bananas", "North", 31.30],
        ["Oranges", "North", 13.10]]

sales = pd.DataFrame(data=data,
                     columns=["Fruit", "Region", "Revenue"])
sales

pivot = pd.pivot_table(sales,
                       index="Fruit", columns="Region",
                       values="Revenue", aggfunc="sum",
                       margins=True, margins_name="Total")
pivot

pd.melt(pivot.iloc[:-1,:-1].reset_index(),
        id_vars="Fruit",
        value_vars=["North", "South"], value_name="Revenue")

## Plotting

### Matplotlib

import numpy as np
%matplotlib inline
# Or %matplotlib notebook

data = pd.DataFrame(data=np.random.rand(4, 4) * 100000,
                    index=["Q1", "Q2", "Q3", "Q4"],
                    columns=["East", "West", "North", "South"])
data.index.name = "Quarters"
data.columns.name = "Region"
data

data.plot()  # Shortcut for data.plot.line()

### Plotly

# Set the plotting backend to Plotly
pd.options.plotting.backend = "plotly"

data.plot()

# Display the same data as bar plot
data.plot.bar(barmode="group")

## Data Import and Export

### Exporting to a CSV file

df.to_csv("course_participants.csv")

### Importing a CSV file

msft = pd.read_csv("csv/MSFT.csv")

msft.info()

# I am selecting a few columns because of space issues
# You can also just run: msft.head()
msft.loc[:, ["Date", "Adj Close", "Volume"]].head()

msft.loc[:, ["Date", "Adj Close", "Volume"]].tail(2)

msft.loc[:, ["Adj Close", "Volume"]].describe()

# The line break in the URL is only to make it fit on the page
url = ("https://raw.githubusercontent.com/fzumstein/"
       "python-for-excel/1st-edition/csv/MSFT.csv")
msft = pd.read_csv(url)

msft.loc[:, ["Date", "Adj Close", "Volume"]].head(2)