#/usr/bin/env python
#from __future__ import absolute_import, division, print_function, unicode_literals

""" Example of browsing for a service (in this case, HTTP) """
import os
import logging
import socket
import sys
import time
import re
from inspect import getsourcefile
from os.path import abspath
import module.FindZeroconfServiceTypes as fs
from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf

def on_service_state_change(zeroconf, service_type, name, state_change):

    path_str = abspath(getsourcefile(lambda:0))
    path_split = path_str.rsplit('/', 2)
    services_file = os.path.join(path_split[0] + "/" + "Data" + "/" + "Essen_files" + "/" + ("camera_list.txt"))
    
    print("Service %s of type %s state changed: %s" % (name, service_type, state_change))

    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            if service_type == "_http._tcp.local.":
                pattern = re.compile(r'^DCS')
                match = pattern.match(info.name)
                if match:
	            with open(services_file, 'ab+') as p1:
	                str1 = (info.name)
	                str2 = ('_')
	                # convert to string type for file writing
                        p1.write("%s:%s:%s" % (str1[0:(str1.find(str2))], socket.inet_ntoa(info.address), info.port))
                        # add a new line
                        p1.write('\n')
		    #dict_info = {'Address':socket.inet_ntoa(info.address), 'port':info.port, 'Weight':info.weight, 'priority':info.priority, 'Server':info.server}
		    print("  Address: %s:%d" % (socket.inet_ntoa(info.address), info.port))
		    print("  Weight: %d, priority: %d" % (info.weight, info.priority))
		    print("  Server: %s" % (info.server,))
	if info.properties:
            print("  Properties are:")
            for key, value in info.properties.items():
                #dict_properties = {'Properties_key':key, 'Properties_value':value}
            	print("    %s: %s" % (key, value))
	print('\n')
#	print(dict_info)
#	print(dict_properties)
		
def service_browser(module_name):

#	str_GetServ, mod_GetServ = fs.get_service()

        path_str = abspath(getsourcefile(lambda:0))
        path_split = path_str.rsplit('/', 2)
        
#	root = "D:\\"
#	services_file = os.path.join(root,"python2","services.txt")
	services_file = os.path.join(path_split[0] + "/" + "Data" + "/" + "Essen_files" + "/" + ("%s.txt" % module_name))
        with open(services_file) as file_object:
            result = list()
            while True:
                line = file_object.readline()
                if not line: break
                result.append(line)
	
	for item in result:
		dlink = str(item)
		dlink = dlink.strip()
		
		logging.basicConfig(level=logging.DEBUG)
		if len(sys.argv) > 1:
			assert sys.argv[1:] == ['--debug']
			logging.getLogger('zeroconf').setLevel(logging.DEBUG)
	
		zeroconf = Zeroconf()
		print("\nBrowsing services, press Ctrl-C to exit...\n")
		browser = ServiceBrowser(zeroconf, dlink, handlers=[on_service_state_change])
		
		time.sleep(3)
		zeroconf.close()
