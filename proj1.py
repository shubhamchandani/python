#!/usr/bin/python
import os
import datetime
import webbrowser
import urllib2
print ("1. to check date and time")
print ("2. to create a file")
print ("3. to create a directory")
print ("4. to search something")
print ("5. to logout system")
print ("6. to shutdown OS")
print ("7. to check internet connection")    
print ("8. to login whatsapp on browser")
print ("9. to check all connected IP in network")

selection  = input("enter the above operation")
if selection == 1:
	current = datetime.datetime.now()
	print (current.strftime("Date : %Y-%m-%d \n Time : %H:%M:%S"))

elif selection == 2:
	file_name = str(raw_input("Enter file name"))
	os.mknod(file_name)

elif selection == 3:
	dir_name = raw_input("Enter the directory name with path")
	os.mkdir(dir_name)

elif selection == 4:
	print ("searching on google")
	search = raw_input("enter your search")
	webbrowser.open_newtab('https"//www.google.com/search?q='+search)

elif selection == 5:
	os.system("exit")

elif selection == 6:
	os.system("shutdown -P")

elif selection == 7:
	try:
		urllib2.urlopen("https://www.google.com/")
	except urllib2.URLError, e:
		print "Network down."
	else:
		print "Connected"





	
