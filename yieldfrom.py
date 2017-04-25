#The 'yield from' expression allows a generator to delegate part of its operations to another 
# generator/iterator or any iterable for that matter.
# It enables you to easily refactor a generator by splitting it up into multiple generators.


# 'yield from' is a shortcut for writing something like this:

def generator1():
    for item in generator2():
        yield item
    #rest of the logic goes here.

# Which can now be written as:
def generator1():
	yield from generator2()


# Here's an example:
def g(x):
	yield from range(x, 0, -1)
	yield from range(x)
	yield from ['a','b','c','d']

print(list(g(5)))