# Appendix C
## Classes and Objects

class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed

    def accelerate(self, mph):
        self.speed += mph

# Let's instantiate two car objects
car1 = Car("red")
car2 = Car(color="blue")

# By default, an object prints its memory location
car1

# Attributes give you access to the data of an object
car1.color

car1.speed

# Calling the accelerate method on car1
car1.accelerate(20)

# The speed attribute of car1 changed
car1.speed

# The speed attribute of car2 remained the same
car2.speed

car1.color = "green"

car1.color

car2.color  # unchanged

## Working with time-zone-aware datetime objects

import datetime as dt
from dateutil import tz

# Time-zone-naive datetime object
timestamp = dt.datetime(2020, 1, 31, 14, 30)
timestamp.isoformat()

# Time-zone-aware datetime object
timestamp_eastern = dt.datetime(2020, 1, 31, 14, 30,
                                tzinfo=tz.gettz("US/Eastern"))
# Printing in isoformat makes it easy to
# see the offset from UTC
timestamp_eastern.isoformat()

# Assign a time zone to a naive datetime object
timestamp_eastern = timestamp.replace(tzinfo=tz.gettz("US/Eastern"))
timestamp_eastern.isoformat()

# Convert from one time zone to another.
# Since the UTC time zone is so common,
# there is a shortcut: tz.UTC
timestamp_utc = timestamp_eastern.astimezone(tz.UTC)
timestamp_utc.isoformat()

# From time-zone-aware to naive
timestamp_eastern.replace(tzinfo=None)

# Current time without time zone
dt.datetime.now()

# Current time in UTC time zone
dt.datetime.now(tz.UTC)

## Mutable vs. Immutable Objects

a = [1, 2, 3]
b = a
a[1] = 22
print(a)
print(b)

a = [1, 2, 3]
b = a.copy()

a

b

a[1] = 22  # Changing "a"...

a

b  # ...doesn't affect "b"

import copy
b = copy.deepcopy(a)

def increment(x):
    x = x + 1
    return x

a = 1
print(increment(a))
print(a)

def increment(x):
    x[0] = x[0] + 1
    return x

a = [1]
print(increment(a))
print(a)

a = [1]
print(increment(a.copy()))
print(a)

# Don't do this:
def add_one(x=[]):
    x.append(1)
    return x

add_one()

add_one()

def add_one(x=None):
    if x is None:
        x = []
    x.append(1)
    return x

add_one()

add_one()