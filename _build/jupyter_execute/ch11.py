# Ch11 The Python Package Tracker

## Core Functionality

### Web APIs

import json

# A Python dictionary...
user_dict = {"name": "Jane Doe",
             "age": 23,
             "married": False,
             "children": None,
             "hobbies": ["hiking", "reading"]}

# ...converted to a JSON string
# by json.dumps ("dump string"). The "indent" parameter is
# optional and prettifies the printing.
user_json = json.dumps(user_dict, indent=4)
print(user_json)

# Convert the JSON string back to a native Python data structure
json.loads(user_json)

import requests

response = requests.get("https://pypi.org/pypi/pandas/json")
response.status_code

# response.json()

releases = []
for version, files in response.json()['releases'].items():
    releases.append(f"{version}: {files[0]['upload_time']}")
releases[:3]  # show the first 3 elements of the list

### Databases

import urllib.parse

urllib.parse.quote_plus("pa$$word")

# Let's start with the imports
import sqlite3
from sqlalchemy import create_engine
import pandas as pd

# Our SQL query: "select all columns from the packages table"
sql = "SELECT * FROM packages"

# Option 1: Database driver (sqlite3 is part of the standard library)
# Using the connection as context manager automatically commits
# the transaction or rolls it back in case of an error.
with sqlite3.connect("packagetracker/packagetracker.db") as con:
    cursor = con.cursor()  # We need a cursor to run SQL queries
    result = cursor.execute(sql).fetchall()  # Return all records
result

# Option 2: SQLAlchemy
# "create_engine" expects the connection string of your database.
# Here, we can execute a query as a method of the connection object.
engine = create_engine("sqlite:///packagetracker/packagetracker.db")
with engine.connect() as con:
    result = con.execute(sql).fetchall()
result

# Option 3: pandas
# Providing a table name to "read_sql" reads the full table.
# Pandas requires an SQLAlchemy engine that we reuse from
# the previous example.
df = pd.read_sql("packages", engine, index_col="package_id")
df

# "read_sql" also accepts an SQL query
pd.read_sql(sql, engine, index_col="package_id")

# The DataFrame method "to_sql" writes DataFrames to tables
# "if_exists" has to be either "fail", "append" or "replace"
# and defines what happens if the table already exists
df.to_sql("packages2", con=engine, if_exists="append")

# The previous command created a new table "packages2" and
# inserted the records from the DataFrame df as we can
# verify by reading it back
pd.read_sql("packages2", engine, index_col="package_id")

# Let's get rid of the table again by running the
# "drop table" command via SQLAlchemy
with engine.connect() as con:
    con.execute("DROP TABLE packages2")

# Let's start by importing SQLAlchemy's text function
from sqlalchemy.sql import text

# ":package_id" is the placeholder
sql = """
SELECT v.uploaded_at, v.version_string
FROM packages p
INNER JOIN package_versions v ON p.package_id = v.package_id
WHERE p.package_id = :package_id
ORDER BY v.uploaded_at
"""

# Via SQLAlchemy
with engine.connect() as con:
    result = con.execute(text(sql), package_id=1).fetchall()
result[:3]  # Print the first 3 records

# Via pandas
pd.read_sql(text(sql), engine, parse_dates=["uploaded_at"],
            params={"package_id": 1},
            index_col=["uploaded_at"]).head(3)

### Exceptions

def print_reciprocal(number):
    result = 1 / number
    print(f"The reciprocal is: {result}")

print_reciprocal(0)  # This will raise an error

def print_reciprocal(number):
    try:
        result = 1 / number
    except Exception as e:
        # "as e" makes the Exception object available as variable "e"
        # "repr" stands for "printable representation" of an object
        # and gives you back a string with the error message
        print(f"There was an error: {repr(e)}")
        result = "N/A"
    else:
        print("There was no error!")
    finally:
        print(f"The reciprocal is: {result}")

print_reciprocal(10)

print_reciprocal("a")

print_reciprocal(0)

def print_reciprocal(number):
    try:
        result = 1 / number
        print(f"The reciprocal is: {result}")
    except (TypeError, ZeroDivisionError):
        print("Please type in any number except 0.")

print_reciprocal("a")

def print_reciprocal(number):
    try:
        result = 1 / number
        print(f"The reciprocal is: {result}")
    except TypeError:
        print("Please type in a number.")
    except ZeroDivisionError:
        print("The reciprocal of 0 is not defined.")

print_reciprocal("a")

print_reciprocal(0)