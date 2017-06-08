#Event maintains a flag that is turns the flag to true if the event is set (set()) and to  False when the event is cleared (clear())

import threading
e=threading.Event()

#Event_Flag shows the current value
print(e.__dict__)

#Set the flag to True:
e.set()
print(e.__dict__)

#Turns the flag to False:
e.clear()
print(e.__dict__)