import shutil, os

#copy files to same/different folders
shutil.copy('a.txt','../a.txt')

#make a copy of the complete directory structure
shutil.copytree('Pandas','Bears')

#move files
shutil.move('abc.txt','../abc.txt')

#delete files
os.unlink('org_copy.py')

#delete folders
os.rmdir('Bears')

#delete folder and everything within it
shutil.rmtree('Bears')

#list filenames in the folder:
os.listdir()

#function to delete all the .csv files in the folder:
def delcsv(): 
	for filename in os.listdir():  
		if filename.endswith('.csv'):   
			print('Deleting this file...')   
			print(filename)   
			os.unlink(filename)  
			print(filename)
delcsv()   

#send2trash module for safe delete
import send2trash
send2trash.send2trash('org_copy.py')

#Walk through a folder:

#for Python 3.5+:

for foldernm,subfolnm,filenm in os.walk('.',topdown=False): 
	print('Foldername: '+foldernm)
	for name in subfolnm:  
		print(os.path.join(foldernm,name))
	for name in filenm:  
		print(os.path.join(foldernm,name))

#for Python 2.7

for foldernm,subfolnm,filenm in os.walk('C:\Users\shilpa.amberker\Documents\PythonFiles'): 
	print('Foldername: '+foldernm) 
	for name in subfolnm:  
		print(os.path.join(foldernm,name))
	for name in filenm:  
		print(os.path.join(foldernm,name))

#Working with Zipfile module:
import zipfile

#creating and adding a file to zip
newzip = zipfile.ZipFile('newone.zip','w')      			 #creates and opens in write mode
newzip.write('test.txt',compress_type=zipfile.ZIP_DEFLATED)  #adds the file in first argument using 'deflate' compression algorithm
newzip.close()

#extracting from zip
existingzip = zipfile.ZipFile('newone.zip')
existingzip.extractall()
existingzip.close()

#Reading zip files
nzip = zipfile.ZipFile('newone.zip')
nzip.namelist()info = nzip.getinfo('test.txt')
info.file_size
info.compress_size
nzip.close()