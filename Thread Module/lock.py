import threading

lock = threading.Lock()

def func(val): 
	with lock:      #A better approach instead of enclosing the code into lock.acquire() and lock.release()  
		print(val)  
		f.write('\n'+val)

list_names=['Bob','Alen','Scott','Chad']

threads = []
f = open('textfile.txt','w') 
for each in list_names: 
	t = threading.Thread(target=func, args=(each, )) 
	threads.append(t) 
	t.start()

while threading.activeCount() > 1: 
	pass
else: 
	f.close()