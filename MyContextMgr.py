#Writing your own context manager using the decorator @contextmanager
from contextlib import contextmanager

@contextmanager
def ManagedFile(name): 
	try:  
		f = open(name,'w')  
		yield f 
	finally:  
		f.close()

#Another way of doing the same is overriding __enter__ and __exit__ methods in your Class:

class MyContextMgr: 
	def __init__(self,name):  
		self.name = name 
	def __enter__(self):  
		self.file = open(self.name,'w')  
		return self.file 
	def __exit__(self,type,val,tb):  
		if self.file:   
			self.file.close()

with MyContextMgr('junk.txt') as f: 
	f.write('Written from MyContextMgr Class') 

with open('junk.txt') as fl: 
	cont = fl.read()  
	print(cont) 

with ManagedFile('junk.txt') as f1: 
	f1.write('Witten from the contextmanager Decorator')

with open('junk.txt') as file: 
	cont = file.read()  
	print(cont)