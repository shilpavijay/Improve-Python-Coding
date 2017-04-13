# Python 3
# Here's a way of merging two dictionaries with a single expression in Python 3.
# x.update(y) is another way doing the same but it does not return the newly 
# constucted dictionary; and another line of code is required to print it.

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

print({**x, **y})



## In Python 2.x you could
# use this:
z = dict(x, **y)
print(z)
{'a': 1, 'c': 4, 'b': 3}