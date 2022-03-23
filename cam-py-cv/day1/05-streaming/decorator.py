#!/usr/bin/python3
# https://stackoverflow.com/questions/308999/what-does-functools-wraps-do

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

"""
def f(x):
    return x + x * x 

f = logged(f)
"""


"""
@logged
def f(x):
   return x + x * x 
"""

print(f(3))

