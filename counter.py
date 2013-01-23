from connection import *

class Counter (object):
  instance = None
  connected=0
  closed=0
  con=""      
  def __new__(cls, *args, **kargs): 
    if cls.instance is None:
      cls.instance = object.__new__(cls, *args, **kargs)
    return cls.instance
  def newConnection(self):
	  print "connection"
  def setConnected(self,con):
    self.connected=con
  def getConnected(self):
    return self.connected
  def setClosed(self,clos):
    self.closed=close
  def getClosed(self):
    return self.closed
    
  def notify_alive(self):
	  self.connected+=1
	  
	  
  def notify_death(self):
	  self.connected-=1	
	  self.closed+=1
	  
