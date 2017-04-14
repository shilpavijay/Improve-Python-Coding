# In a plain tuple, data stored can only be retrieved using indexes. You can’t give names to individual properties 
# stored in a tuple. This can impact code readability. Named Tuples come to the resue

# Named Tuples are also immutable just like regular tuples. Each object store can be accessible through a unique
# identifier. Hence makes it very readable.

# Namedtuples are a memory-efficient shortcut to defining an IMMUTABLE CLASS in Python manually. 

from collections import namedtuple
import json

Emp = namedtuple('person',['name','age'])

emp1 = Emp('bob',23)

print(Emp)
print(emp1)
print(emp1.name, emp1.age)

emp2 = Emp('Alice',12)
emp3 = Emp('John',44)
emp4 = Emp('Mary',24)

#unpacking Named Tuples:

nm,age = emp2
print(nm,age)

# OR

print(*emp3)  # Function argument unpacking

# You can still use indices:

print(emp4[0],emp4[1])

# can convert it into plain tuple:

print(tuple(emp4))

# HELPER METHODS:

# The _asdict() helper returns the contents of a namedtuple as a dictionary:

print(emp4._asdict())

#JSON output:

print(json.dumps(emp4._asdict()))

# _replace() function creates a shallow copy of a tuple and allows you to selectively replace some of its fields:

emp4copy = emp4._replace(name='Jamie')
print(*emp4copy)