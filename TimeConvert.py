import time, datetime 
from datetime import date, timedelta

def unix_to_datetime(val): 
	return time.ctime(int(val))

def datetime_to_unix_tmstmp(s,format): 
	return time.mktime(datetime.datetime.strptime(s, format).timetuple())

def get_unix_ts_btw_dates(frm,to): 
	unix_tm = {} 
	frm = frm.split('/') 
	to = to.split('/') 
	frm = date(int(frm[2]),int(frm[1]),int(frm[0])) 
	to = date(int(to[2]),int(to[1]),int(to[0])) 
	delta = to - frm 
	for n in range (delta.days + 1):  
		dt = str(frm+timedelta(days=n))  
		unix_tm[dt] = datetime_to_unix_tmstmp(dt,"%Y-%m-%d") 
	return unix_tm
	
print (unix_to_datetime("1494009000"))
print (datetime_to_unix_tmstmp("06/05/2017","%d/%m/%Y"))
print (get_unix_ts_btw_dates('06/05/2017','08/05/2017'))

