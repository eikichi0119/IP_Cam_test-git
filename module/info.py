#!/usr/bin/env python
import requests
import module_name as MN
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup
import time
from inspect import getsourcefile
from os.path import abspath
import os

def info():
    module_name = MN.info()
    module_name = module_name.strip()
    module_name = module_name.split('.')[1]

    path_str = abspath(getsourcefile(lambda:0))
    path_split = path_str.rsplit('/', 2)
    camera_list = os.path.join(path_split[0] + "/" + "Data" + "/" + "Essen_files" + "/" +("camera_list.txt"))

    str_1 = 0
    str_2 = 0
    str_3 = 0
    str_4 = 0

    cam_response = []
    cam_soup = []
    cam_soupbody = []
    with open(camera_list, 'rb') as camera_info:
	model = []
	address = []
	port = []
	for line in camera_info.readlines():
        	line = str(line.strip())
		list1 = line.split(":")
		model.append(list1[0])
		address.append(list1[1])
		port.append(list1[2])
    cams = len(model)

    for i in range(cams):
        url = ("http://%s:%s/common/info.cgi" % (address[i], port[i]))
        response = requests.get(url, auth=('admin', ''))
        str_1 = str(response)
        # connect
        if str_1 == ("<Response [401]>"):
            print ("Wrong password.")
            time.sleep(3)
            url = ("http://%s:%s/common/info.cgi" % (address[i], port[i]))
            response = requests.get(url, auth=('admin', 'admin'))
            str_2 = str(response)

        if str_2 == ("<Response [401]>"):
            print ("Digest needed.")
            time.sleep(3)
            url = ("http://%s:%s/common/info.cgi" % (address[i], port[i]))
            response = requests.get(url, auth=HTTPDigestAuth('admin', ''))
            str_3 = str(response)

        if str_3 == ("<Response [401]>"):
            print  ("Password in digest needed.")
            time.sleep(3)
            url = ("http://%s:%s/common/info.cgi" % (address[i], port[i]))
            response = requests.get(url, auth=HTTPDigestAuth('admin', 'admin'))
            str_4 = str(response)
            
        cam_response.append(str(response))
        # get text parts of DUT response
        html = response.text
        # parsing with Beautifulsoup
        soup = BeautifulSoup(html, 'html.parser')
        
        cam_soup.append(str(soup))
        cam_soupbody.append(str(soup.body))
    return (cams, model, address, port, cam_response, cam_soup, cam_soupbody, module_name)
