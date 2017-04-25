# Here's a list of lists with uneven number of elements in each of them.
# We will flatten it into a single list.

l = [[21],[9,33,12,4,5],[1,2],[4,3]]

import functools

print(functools.reduce(lambda x,y: x+y,l))

#If the number of elements in the list were same, the solution below would also work:

l = [[1,2],[34,23],[4,5]]

flatl = [j for i in l for j in i]
print(flatl)


# What if the list is multi-level?
# Here's a solution:

l = [[21,[3,4]],[9,33,12,[4,5]],[1,2],[4,3]]

def flatten(l):
    for each in l:
        try:
            yield from flatten(each)
        except TypeError:
            yield each

print(list(flatten(l)))