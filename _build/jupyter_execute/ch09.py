# Ch09 Excel Automation

## Getting Started with xlwings

### Using Excel as Data Viewer

# First, let's import the packages that we"ll use in this chapter
import datetime as dt
import xlwings as xw
import pandas as pd
import numpy as np

# Let's create a DataFrame based on pseudorandom numbers and
# with enough rows that only the head and tail are shown
df = pd.DataFrame(data=np.random.randn(100, 5),
                  columns=[f"Trial {i}" for i in range(1, 6)])
df

# View the DataFrame in Excel
xw.view(df)

### The Excel Object Model

# Create a new empty workbook and print its name. This is the
# book we will use to run most of the code samples in this chapter.
book = xw.Book()
book.name

# Accessing the sheets collection
book.sheets

# Get a sheet object by index or name. You will need to adjust
# "Sheet1" if your sheet is called differently.
sheet1 = book.sheets[0]
sheet1 = book.sheets["Sheet1"]

sheet1.range("A1")

# Most common tasks: write values...
sheet1.range("A1").value = [[1, 2],
                            [3, 4]]
sheet1.range("A4").value = "Hello!"

# ... and read values
sheet1.range("A1:B2").value

sheet1.range("A4").value

# Indexing
sheet1.range("A1:B2")[0, 0]

# Slicing
sheet1.range("A1:B2")[:, 1]

# Single cell: A1 notation
sheet1["A1"]

# Multiple cells: A1 notation
sheet1["A1:B2"]

# Single cell: indexing
sheet1[0, 0]

# Multiple cells: slicing
sheet1[:2, :2]

# D10 via sheet indexing
sheet1[9, 3]

# D10 via range object
sheet1.range((10, 4))

# D10:F11 via sheet slicing
sheet1[9:11, 3:6]

# D10:F11 via range object
sheet1.range((10, 4), (11, 6))

sheet1["A1"].sheet.book.app

# Get one app object from the open workbook
# and create an additional invisible app instance
visible_app = sheet1.book.app
invisible_app = xw.App(visible=False)

# List the book names that are open in each instance
# by using a list comprehension
[book.name for book in visible_app.books]

[book.name for book in invisible_app.books]

# An app key represents the process ID (PID)
xw.apps.keys()

# It can also be accessed via the pid attribute
xw.apps.active.pid

# Work with the book in the invisible Excel instance
invisible_book = invisible_app.books[0]
invisible_book.sheets[0]["A1"].value = "Created by an invisible app."

# Save the Excel workbook in the xl directory
invisible_book.save("xl/invisible.xlsx")

# Quit the invisible Excel instance
invisible_app.quit()

### Running VBA Code

vba_book = xw.Book("xl/vba.xlsm")

# Instantiate a macro object with the VBA function
mysum = vba_book.macro("Module1.MySum")
# Call a VBA function
mysum(5, 4)

# It works the same with a VBA Sub procedure
show_msgbox = vba_book.macro("Module1.ShowMsgBox")
show_msgbox("Hello xlwings!")

# Close the book again (make sure to close the MessageBox first)
vba_book.close()

## Converters, Options and Collections

### Working with DataFrames

data=[["Mark", 55, "Italy", 4.5, "Europe"],
      ["John", 33, "USA", 6.7, "America"]]
df = pd.DataFrame(data=data,
                  columns=["name", "age", "country",
                           "score", "continent"],
                  index=[1001, 1000])
df.index.name = "user_id"
df

sheet1["A6"].value = df

sheet1["B10"].options(header=False, index=False).value = df

df2 = sheet1["A6"].expand().options(pd.DataFrame).value
df2

# If you want the index to be an integer index,
# you can change its data type
df2.index = df2.index.astype(int)
df2

# By setting index=False, it will put all the values from Excel into
# the data part of the DataFrame and will use the default index
sheet1["A6"].expand().options(pd.DataFrame, index=False).value

### Converters and Options

# Horizontal range (one-dimensional)
sheet1["A1:B1"].value

# Vertical range (one-dimensional)
sheet1["A1:A2"].value

# Horizontal range (two-dimensional)
sheet1["A1:B1"].options(ndim=2).value

# Vertical range (two-dimensional)
sheet1["A1:A2"].options(ndim=2).value

# Using the NumPy array converter behaves the same:
# vertical range leads to a one-dimensional array
sheet1["A1:A2"].options(np.array).value

# Preserving the column orientation
sheet1["A1:A2"].options(np.array, ndim=2).value

# If you need to write out a list vertically,
# the "transpose" option comes in handy
sheet1["D1"].options(transpose=True).value = [100, 200]

# Write out some sample data
sheet1["A13"].value = [dt.datetime(2020, 1, 1), None, 1.0]

# Read it back using the default options
sheet1["A13:C13"].value

# Read it back using non-default options
sheet1["A13:C13"].options(empty="NA",
                          dates=dt.date,
                          numbers=int).value

### Charts, Pictures and Defined Names

sheet1["A15"].value = [[None, "North", "South"],
                       ["Last Year", 2, 5],
                       ["This Year", 3, 6]]

chart = sheet1.charts.add(top=sheet1["A19"].top,
                          left=sheet1["A19"].left)
chart.chart_type = "column_clustered"
chart.set_source_data(sheet1["A15"].expand())

# Read in the chart data as DataFrame
df = sheet1["A15"].expand().options(pd.DataFrame).value
df

# Enable Matplotlib by using the notebook magic command
# and switch to the "seaborn" style
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn")

# The pandas plot method returns an "axis" object from 
# where you can get the figure. "T" transposes the
# DataFrame to bring the plot into the desired orientation.
ax = df.T.plot.bar()
fig = ax.get_figure()

# Send the plot to Excel
plot = sheet1.pictures.add(fig, name="SalesPlot",
                           top=sheet1["H19"].top,
                           left=sheet1["H19"].left)
# Let's scale the plot to 70%
plot.width, plot.height = plot.width * 0.7, plot.height * 0.7

ax = (df + 1).T.plot.bar()
plot = plot.update(ax.get_figure())

# The book scope is the default scope
sheet1["A1:B2"].name = "matrix1"

# For the sheet scope, prepend the sheet name with
# an exclamation point
sheet1["B10:E11"].name = "Sheet1!matrix2"

# Now you can access the range by name
sheet1["matrix1"]

# If you access the names collection via the "sheet1" object,
# it contains only names with that sheet's scope
sheet1.names

# If you access the names collection via the "book" object,
# it contains all names, including book and sheet scope
book.names

# Names have various methods and attributes.
# You can, for example, get the respective range object.
book.names["matrix1"].refers_to_range

# If you want to assign a name to a constant
# or a formula, use the "add" method
book.names.add("EURUSD", "=1.1151")

## Advanced Topics

### Performance

# Add a new sheet and write 150 values
# to it to have something to work with
sheet2 = book.sheets.add()
sheet2["A1"].value = np.arange(150).reshape(30, 5)

%%time
# This makes 150 cross-application calls
for cell in sheet2["A1:E30"]:
    cell.value += 1

%%time
# This makes just two cross-application calls
values = sheet2["A1:E30"].options(np.array).value
sheet2["A1"].value = values + 1

# With raw values, you must provide the full
# target range, sheet["A35"] doesn't work anymore
sheet1["A35:B36"].options("raw").value = [[1, 2], [3, 4]]