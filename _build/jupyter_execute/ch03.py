# Ch03 Getting Started with Python

## Data Types

### Variables

a = 3
b = 4
a + b

a = 3
print(a)
a = "three"
print(a)

### Numeric Types

type(4)

type(4.4)

type(4.)

float(4)

int(4.9)

1.125 - 1.1

3 + 4  # Sum

3 - 4  # Subtraction

3 / 4  # Division

3 * 4  # Multiplication

3**4  # The power operator (Excel uses 3^4)

3 * (3 + 4)  # Use of parentheses

### Comments

# This is a sample we've seen before.
# Every comment line has to start with a #
3 + 4

3 + 4  # This is an inline comment

### Booleans

3 == 4  # Equality (Excel uses 3 = 4)

3 != 4  # Inequality (Excel uses 3 <> 4)

3 < 4  # Smaller than. Use > for bigger than.

3 <= 4  # Smaller or equal. Use >= for bigger or equal.

# You can chain logical expressions
# In VBA, this would be: 10 < 12 And 12 < 17
# In Excel formulas, this would be: =AND(10 < 12, 12 < 17)
10 < 12 < 17

not True  # "not" operator

False and True  # "and" operator

False or True  # "or" operator

bool(2)

bool(0)

bool("some text")  # We'll get to strings in a moment

bool("")

bool(None)

### Strings

"A double quote string. " + 'A single quote string.'

print("Don't wait! " + 'Learn how to "speak" Python.')

print("It's easy to \"escape\" characters with a leading \\.")

# Note how Python allows you to conveniently assign multiple
# values to multiple variables in a single line
first_adjective, second_adjective = "free", "open source"
f"Python is {first_adjective} and {second_adjective}."

"PYTHON".lower()

"python".upper()

## Indexing and Slicing

language = "PYTHON"

language[0]

language[1]

language[-1]

language[-2]

language[:3]  # Same as language[0:3]

language[1:3]

language[-3:]  # Same as language[-3:6]

language[-3:-1]

language[::2]  # Every second element

language[-1:-4:-1]  # Negative step goes from right to left

language[-3:][1]

## Data Structures

### Lists

file_names = ["one.xlsx", "two.xlsx", "three.xlsx"]
numbers = [1, 2, 3]

file_names + numbers

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

cells = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

cells[1]  # Second row

cells[1][1:]  # Second row, second and third column

### Line Continuation

a = (1 + 2
     + 3)

a = 1 + 2 \
    + 3

users = ["Linda", "Brian"]

users.append("Jennifer")  # Most commonly you add to the end
users

users.insert(0, "Kim")  # Insert "Kim" at index 0 
users

users.pop()  # Removes and returns the last element by default

users

del users[0]  # del removes an element at the given index

len(users)  # Length

"Linda" in users  # Check if users contains "Linda"

print(sorted(users))  # Returns a new sorted list
print(users)  # The original list is unchanged

users.sort()  # Sorts the original list
users

len("Python")

"free" in "Python is free and open source."

### Dictionaries

exchange_rates = {"EURUSD": 1.1152,
                  "GBPUSD": 1.2454,
                  "AUDUSD": 0.6161}

exchange_rates["EURUSD"]  # Access the EURUSD exchange rate

exchange_rates["EURUSD"] = 1.2  # Change an existing value
exchange_rates

exchange_rates["CADUSD"] = 0.714  # Add a new key/value pair
exchange_rates

{**exchange_rates, **{"SGDUSD": 0.7004, "GBPUSD": 1.2222}}

currencies = {1: "EUR", 2: "USD", 3: "AUD"}

currencies[1]

# currencies[100] would raise an exception. Instead of 100,
# you could use any other non-existing key, too.
currencies.get(100, "N/A")

### Tuple

currencies = ("EUR", "GBP", "AUD")

currencies[0]  # Accessing the first element

# Concatenating tuples will return a new tuple.
currencies + ("SGD",)

### Set

set(["USD", "USD", "SGD", "EUR", "USD", "EUR"])

portfolio1 = {"USD", "EUR", "SGD", "CHF"}
portfolio2 = {"EUR", "SGD", "CAD"}

# Same as portfolio2.union(portfolio1)
portfolio1.union(portfolio2)

# Same as portfolio2.intersection(portfolio1)
portfolio1.intersection(portfolio2)

### Summary

currencies = "USD", "EUR", "CHF"
currencies

list(currencies)

## Control Flow

### If Statement

i = 20
if i < 5:
    print("i is smaller than 5")
elif i <= 10:
    print("i is between 5 and 10")
else:
    print("i is bigger than 10")

is_important = True
if is_important:
    print("This is important.")
else:
    print("This is not important.")

values = []
if values:
    print(f"The following values were provided: {values}")
else:
    print("There were no values provided.")

is_important = False
print("important") if is_important else print("not important")

### For and While Loops

currencies = ["USD", "HKD", "AUD"]

for currency in currencies:
    print(currency)

range(5)

list(range(5))  # stop argument

list(range(2, 5, 2))  # start, stop, step arguments

for i in range(3):
    print(i)

for i, currency in enumerate(currencies):
    print(i, currency)

exchange_rates = {"EURUSD": 1.1152,
                  "GBPUSD": 1.2454,
                  "AUDUSD": 0.6161}
for currency_pair in exchange_rates:
    print(currency_pair)

for currency_pair, exchange_rate in exchange_rates.items():
    print(currency_pair, exchange_rate)

for i in range(15):
    if i == 2:
        break
    else:
        print(i)

for i in range(4):
    if i == 2:
        continue
    else:
        print(i)

for i in range(1, 4):
    print(i)
print(i)

n = 0
while n <= 2:
    print(n)
    n += 1

### List, Set and Dictionary Comprehensions

currency_pairs = ["USDJPY", "USDGBP", "USDCHF",
                  "USDCAD", "AUDUSD", "NZDUSD"]

usd_quote = []
for pair in currency_pairs:
    if pair[3:] == "USD":
        usd_quote.append(pair[:3])
usd_quote

[pair[:3] for pair in currency_pairs if pair[3:] == "USD"]

[pair[3:] + pair[:3] for pair in currency_pairs]

exchange_rates = {"EURUSD": 1.1152,
                  "GBPUSD": 1.2454,
                  "AUDUSD": 0.6161}
{k: v * 100 for (k, v) in exchange_rates.items()}

{s + "USD" for s in ["EUR", "GBP", "EUR", "HKD", "HKD"]}

## Code organization

### Functions

def convert_to_celsius(degrees, source="fahrenheit"):
    if source.lower() == "fahrenheit":
        return (degrees-32) * (5/9)
    elif source.lower() == "kelvin":
        return degrees - 273.15
    else:
        return f"Don't know how to convert from {source}"

convert_to_celsius(100, "fahrenheit")  # Positional arguments

convert_to_celsius(50)  # Will use the default source (fahrenheit)

convert_to_celsius(source="kelvin", degrees=0)  # Keyword arguments

### Modules and the Import Statement

import temperature

temperature.TEMPERATURE_SCALES

temperature.convert_to_celsius(120, "fahrenheit")

import temperature as tp

tp.TEMPERATURE_SCALES

from temperature import TEMPERATURE_SCALES, convert_to_celsius

TEMPERATURE_SCALES

### Date and Time

# Import the datetime module as "dt"
import datetime as dt

# Instantiate a datetime object called "timestamp"
timestamp = dt.datetime(2020, 1, 31, 14, 30)
timestamp

# Datetime objects offer various attributes, e.g. to get the day
timestamp.day

# The difference of two datetime objects returns a timedelta object
timestamp - dt.datetime(2020, 1, 14, 12, 0)

# Accordingly, you can also work with timedelta objects
timestamp + dt.timedelta(days=1, hours=4, minutes=11)

# Format a datetime object in a specific way
# You could also use an f-string: f"{timestamp:%d/%m/%Y %H:%M}"
timestamp.strftime("%d/%m/%Y %H:%M")

# Parse a string into a datetime object
dt.datetime.strptime("12.1.2020", "%d.%m.%Y")