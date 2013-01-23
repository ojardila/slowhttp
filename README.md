SlowHttp:

This script works like a Dos attack simulator creating a lot of connections with a server controlling the incoming data , reading it very slow For more information about this mechanism check it http://www.securitybydefault.com/2012/01/slow-read-nuevo-mecanismo-dos-de.html


Usage: ./slowhttpread [OPTIONS]...
  Options: 
	-h, --host	        Specify the destination host	
	-t, --threads	    The threads for complete total connections  	
	-p, --port	    The port where is running the http server  	
	-r, --request       Request for the http method
	-m, --method        HTTP Method, PUT, GET, POST, OPTIONS

	
	
Example:

	./slowhttpread -h 192.168.1.2  -t 200 

	This execution will generate a attack using 200 threads 
