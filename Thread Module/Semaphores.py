import threading
import math

def display(s, val): 
	with s:  
		print(str(val)+ 'is: '+ str(math.sqrt(val))+'\n')  
	return


threads = []
sem = threading.Semaphore(3)
print('Square roots of: ' )

for i in range(1,11): 
	t = threading.Thread(target=display,args=(sem,i)) 
	threads.append(t) 
	t.start()


#Find the current Semaphore value
sem.__dict__       

#Semaphore_value will show the available semaphore value / number of resources available.  

#Acquiring the semaphore:
#If current Semaphore_value is 0 it will wait for some resource to be released.sem.acquire() will Decrement the Semaphore_value by 1

#Release:
sem.release()    #will Increment the Semaphore_value by 1



# BOUNDED SEMAPHORES
# You must have observed that calling release() multiple times can increase the Semaphore_value above the initial value.
# Bounded semaphore restricts this behavior. It raises 'ValueError' if release() increases above the initial value.

t = threading.BoundedSemaphore(3)

#The following raises the exception: "ValueError: Semaphore released too many times"
t.release()
