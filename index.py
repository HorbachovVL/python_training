print('Hello World')

for i in [1, 2, 3]:
    if i == 3:
        print('Number 3 found')
    else:
        print('Number:', i)

# Immutable types (cannot be changed after creation)
some_str = 'some string'
some_int = 15
some_float = 23.23
some_tuple = (13, 45, 'Yo', 34.3)

# Mutable types (can be changed)
some_list = [14, 'string', 14,[1, 2]]
some_set = {(1, 2), 'string', 14}
some_dict = {'name': 'John', 'sname': 'Smith'}

# Basic operators, sequences:
test_string = 'Hello ' + 'World'
print(test_string)
crazy_string = 'Yo' * 10
print(crazy_string)

one_list = ['Ring of elves', 'Ring of dwarves']
all_rings = one_list + ['Ring of men']
print(len(all_rings))
all_rings.append('Ring of Power')
print(all_rings)
# Also: extend(), count(), reverse(), sort()

# Conditions, cycles
a = 5
b = 3
if a > b:
    print('a is greater than b')
else:
    print('something wrong')

for i in range(1, 10):
    print(i)


import math
from math import cos
from random import choice as ch
from math import *

math.cos(180)
cos(49)
ch([1, 2, 4])
pi

# Function
x = 10
def mult(a, b = 5):
    return a * b + x

print(mult(4, 3))
print(mult(4))
print(mult(b = 15, a = 5))
print(mult(10))

a, b = 45, '54'
a, b = b, a
print(a)
print(b)

def testme(my_list):
    my_list.append('end')
    print(my_list)
my_list = [1]
testme(my_list)

class Foo(object):
    attr1 = 'Some value'
    attr2 = 'Boo'

    def __str__(self):
        return 'Nice warm object'
    def foo(self):
        return self.attr1
    def __init__(self, val = None):
        print(f'Initializing new object with val = {val}')
        if val is not None:
            self.attr1 = val

obj = Foo('Super Value')
print(obj)
print('Result of obj.foo():', obj.foo())
print(obj.attr1)
print(obj.attr2)
print(Foo.attr1)
print(obj.foo())