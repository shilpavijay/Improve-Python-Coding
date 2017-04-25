# Python has no explicity Switch-case statement but the same can be implemented with 'if' statements and 
# hence the decision was to not include a separate switch-case statement into Python
# However, we will bring about the same behavior as the switch-case statement in the following code.

def funcA():
	return "I am in A"

def funcB():
	return "I am in B"

d = {'a': funcA, 'b':funcB}

while True:
	choice = input("Enter your choice(options: a or b): ")

	if not choice: break
	elif choice in d:
		print(d[choice]())
	else:
		print('{} is not an option'.format(choice))