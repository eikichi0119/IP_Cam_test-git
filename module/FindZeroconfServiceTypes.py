#!/usr/bin/env python
#coding=UTF-8

from zeroconf import ZeroconfServiceTypes
import module_name as MN
import re
	
def get_service():
	# Open a file
	#fo = open("services.txt", "wb")
	#fo.write('\n'.join(ZeroconfServiceTypes.find()))
        str = ('\n'.join(ZeroconfServiceTypes.find()))
        module_name = MN.info()
        module_name = module_name.strip()
        module_name = module_name.split('.')[1]
        return (str, module_name)
	# Close opend file
	#fo.close()
