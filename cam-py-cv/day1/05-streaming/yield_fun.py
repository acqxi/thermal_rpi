#!/usr/bin/python3
# https://blog.blackwhite.tw/2013/05/python-yield-generator.html

def yield_fun():
    a = 1
    b = 2
    
    yield a
    print(3)
    yield b

gen = yield_fun()
#print(yield_fun())

print(gen.__next__())
print(gen.__next__())

