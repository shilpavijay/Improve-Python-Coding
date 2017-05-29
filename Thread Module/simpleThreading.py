import threading

def get_cube(val): 
  print('cube of '+str(val)+': '+str(val**3)) 
  return 

threads = []
for num in range(1,20):
  t=threading.Thread(target = get_cube, args=(num, )) 
  threads.append(t) 
  t.start()
  