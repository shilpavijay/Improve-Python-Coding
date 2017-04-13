# Python 3
# Here's a way of combining two dictionaries with reduced number of lines.
# x.update(y) is another way doing the same but it does not return the newly 
# constucted dictionary; and another line of code is required to print it.

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

print({**x, **y})