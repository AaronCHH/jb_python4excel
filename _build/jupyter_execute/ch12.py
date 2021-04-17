# Ch12 User-Defined Functions (UDFs)

## Function Decorators

# This is the definition of the function decorator
def verbose(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Using a function decorator
@verbose
def print_hello():
    print("hello!")

# Effect of calling the decorated function
print_hello()

## Fetching Data from Google Trends

from pytrends.request import TrendReq

# First, let's instantiate a TrendRequest object
trend = TrendReq()

# Now we can print the suggestions as they would appear
# online in the dropdown of Google Trends after typing in "Python"
trend.suggestions("Python")

## Caching

import time

cache = {}

def slow_sum(a, b):
    key = (a, b)
    if key in cache:
        return cache[key]
    else:
        time.sleep(2)  # sleep for 2 seconds
        result = a + b
        cache[key] = result
        return result

%%time
slow_sum(1, 2)

%%time
slow_sum(1, 2)