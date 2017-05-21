from collections import deque

q=deque()

#Basic operations:
#Using deque as a Stack
#push into the stack:

q.append("I")
q.append("am")
q.append("a")
q.append("Stack")
q.append("ends here")
q.append(".")
print("\nStack: ")
print(q)

#pop an item from Stack - LIFO obviously:
print("\nPopped item: ")
print(q.pop())


#Other interesting operations
#append left:
print("\nAppend left: ")
q.appendleft("Hi")
print(q)

#pop left:
print("\nPopped item from left: ")
print(q.popleft())

print("\nRotate Right by one step:")
q.rotate()
print(q)

#rotate by one step to the left (reverse the direction)
print("\nRotate Left by one step: ")
q.rotate(-1)
print(q)


print("\nRotate Right by n (=3) steps: ")
q.rotate(3)
print(q)

print("\nRotate Left by n (=3) steps: ")
q.rotate(-3)
print(q)

print("\nInsert an element - 100 at index 2")
q.insert(2,100)
print(q)

print("\nReturn the first index of the value 100:")
print(q.index(100))

print("\nExtend right side of the queue with the elements in an iterable:")
r=deque()
r.append("I am another stack")
q.extend(r)
print(q)

print("\nSimilarly, extent left:")
q.extendleft(r)
print(q)