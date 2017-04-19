# Lets consider the following list of lists:

lst = [[12, 2, 42], [21, 21, 12], [2, 4, 1], [7, 23, 0]]

# How can we sort the list based on the third element by writing a single line of code?
# Here's how we do it:

print(sorted(lst, key = lambda x: x[2]))


# The same can be applied to a python dictionary in order to sort the dictionary based on either key or value
# Lets consider the following dictionary and sort it based on its value:

d = {'b': 4, 'a': 3, 'd': 2, 'c': 1}

print(sorted(d.items(), key = lambda x: x[1]))

# OR
# We could also make use of the operator module:

import operator

print(sorted(d.items(), key = operator.itemgetter(1)))