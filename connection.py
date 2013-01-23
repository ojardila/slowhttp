#!/bin/python

""" 
connection.py contain Connection class
- Connection class
  This class create a connection , connect, disconnect, send messages to a host

"""
import socket,time,sys
import threading
from counter import *

class Connection(threading.Thread):
  options={"host":"192.168.1.6","port":80,"timebetweenrequest":1,"request":"GET / HTTP/1.0\r\n\r\n","response":"","debug":False,"counter":""}


  def run(self):
    con1=Connection()
    con1.connect()
    con1.sendMessage()
    con1.getResponse()
    
  def setOptions(self,options):
    self.options=options.copy() 
  
  def setOption(self,option,value):
	self.options[option]=value
	
  def getOption(self,option):
    return self.options[option]
	
  def getOptions(self):	
    return self.options
  def connect(self):
    try:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
      sys.stderr.write("[ERROR] %s\n" % msg[1])
      sys.exit(1)
      
    try:
      self.sock.connect((self.options['host'], self.options['port']))
      if self.options['debug']:
        print  "[DEBUG] Connecting to %s:%s" %(self.options['host'], self.options['port'])
    except socket.error, msg:
      sys.stderr.write("[ERROR] %s\n" % msg[1])
      sys.exit(2)

  def disconnect(self):
    self.sock.close()
    if self.options['debug']:
      print  "[DEBUG] Disconnecting from %s:%s" %(self.options['host'], self.options['port'])
    

  def sendMessage(self):
    if self.options['debug']:
      print "[DEBUG] Sending data."
    self.sock.send(self.options['request'])
    self.setOption("counter",Counter())
    self.getOption("counter").notify_alive()
  
  
  def getResponse(self):
    if self.options['debug']:
      print "[DEBUG] Getting Slow data.	"
    receive_data=True
    while receive_data:
      try:
        self.options['response']+=self.sock.recv(1)
        self.sock.send(self.options['request'])
        time.sleep(self.options['timebetweenrequest'])
      except socket.error, e:	
        receive_data=False
        self.getOption("counter").notify_death()
        self.getOption("manager").newConnection(self.getOptions())
