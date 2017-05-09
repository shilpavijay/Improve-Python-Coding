# The most Pythonic way of using getters and setters is not to use them at all. 
# However implementing them helps in understanding how Python "descriptors" work. When we retrieve a.b or try to 
# make an assignment a.b = c,# python internally invokes another method in order to perform the assignment.
# When the values assigned to a variable are to be restricted, it can be done the following way using the 
# @propery and the @setter. 

class Books(object): 
	def __init__(self):  
		self._price = 0
 	@property 
 	def price(self):  
 		return self._price
 	@price.setter 
 	def price(self,val):  
 		if val > 1000:   
 			val = 1000  
 			self._price = val

b = Books()
print(b.price)
b.price = 12000
print(b.price)