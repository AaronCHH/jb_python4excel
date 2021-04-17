# Ch06 Time Series Analysis with pandas

## DatetimeIndex

# Let's start by importing the packages we use in this chapter
# and by setting the plotting backend to Plotly
import pandas as pd
import numpy as np
pd.options.plotting.backend = "plotly"

# This creates a DatetimeIndex based on a start timestamp,
# number of periods and frequency ("D" = daily).
daily_index = pd.date_range("2020-02-28", periods=4, freq="D")
daily_index

# This creates a DatetimeIndex based on start/end timestamp.
# The frequency is set to "weekly on Sundays" ("W-SUN").
weekly_index = pd.date_range("2020-01-01", "2020-01-31", freq="W-SUN")
weekly_index

# Construct a DataFrame based on the weekly_index. This could be
# the visitor count of a museum that only opens on Sundays.
pd.DataFrame(data=[21, 15, 33, 34],
             columns=["visitors"], index=weekly_index)

msft = pd.read_csv("csv/MSFT.csv")

msft.info()

msft.loc[:, "Date"] = pd.to_datetime(msft["Date"])

msft.dtypes

msft = pd.read_csv("csv/MSFT.csv",
                   index_col="Date", parse_dates=["Date"])

msft.info()

msft.loc[:, "Volume"] = msft["Volume"].astype("float")
msft["Volume"].dtype

msft = msft.sort_index()

msft.index.date

msft.loc["2019", "Adj Close"]

msft.loc["2019-06":"2020-05", "Adj Close"].plot()

### Working with Time Zones

# Add the time information to the date
msft_close = msft.loc[:, ["Adj Close"]].copy()
msft_close.index = msft_close.index + pd.DateOffset(hours=16)
msft_close.head(2)

# Make the timestamps time-zone-aware
msft_close = msft_close.tz_localize("America/New_York")
msft_close.head(2)

msft_close = msft_close.tz_convert("UTC")
msft_close.loc["2020-01-02", "Adj Close"]  # 21:00 without DST

msft_close.loc["2020-05-01", "Adj Close"]  # 20:00 with DST

## Common Time Series Manipulations

### Shifting and Percentage Changes

msft_close.head()

msft_close.shift(1).head()

returns = np.log(msft_close / msft_close.shift(1))
returns = returns.rename(columns={"Adj Close": "returns"})
returns.head()

# Plot a histogram with the daily log returns
returns.plot.hist()

simple_rets = msft_close.pct_change()
simple_rets = simple_rets.rename(columns={"Adj Close": "simple rets"})
simple_rets.head()

### Rebasing and Correlation

parts = []  # List to collect individual DataFrames
for ticker in ["AAPL", "AMZN", "GOOGL", "MSFT"]:
  # "usecols" allows us to only read in the Date and Adj Close
  adj_close = pd.read_csv(f"csv/{ticker}.csv",
                          index_col="Date", parse_dates=["Date"],
                          usecols=["Date", "Adj Close"])
  # Rename the column into the ticker symbol
  adj_close = adj_close.rename(columns={"Adj Close": ticker})
  # Append the stock's DataFrame to the parts list
  parts.append(adj_close)

# Combine the 4 DataFrames into a single DataFrame
adj_close = pd.concat(parts, axis=1)
adj_close

adj_close = adj_close.dropna()
adj_close.info()

# Use a sample from June 2019 - May 2020
adj_close_sample = adj_close.loc["2019-06":"2020-05", :]
rebased_prices = adj_close_sample / adj_close_sample.iloc[0, :] * 100
rebased_prices.head(2)

rebased_prices.plot()

# Correlation of daily log returns
returns = np.log(adj_close / adj_close.shift(1))
returns.corr()

import plotly.express as px

fig = px.imshow(returns.corr(),
                x=adj_close.columns,
                y=adj_close.columns,
                color_continuous_scale=list(
  reversed(px.colors.sequential.RdBu)),
  zmin=-1, zmax=1)
fig.show()

### Resampling

end_of_month = adj_close.resample("M").last()
end_of_month.head()

end_of_month.resample("D").asfreq().head()  # No transformation

end_of_month.resample("W-FRI").ffill().head()  # Forward fill

### Rolling Windows

# Plot the moving average for MSFT with data from 2019
msft19 = msft.loc["2019", ["Adj Close"]].copy()
# Add the 25 day moving average as a new column to the DataFrame
msft19.loc[:, "25day average"] = msft19["Adj Close"].rolling(25).mean()
msft19.plot()