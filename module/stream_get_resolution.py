#!/usr/bin/env python
import requests
import module_name as MN
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup
import time
from inspect import getsourcefile
from os.path import abspath
import os
import re

def get_resolution(cams, model, address, port):
    module_name = MN.info()
    module_name = module_name.strip()
    module_name = module_name.split('.')[1]

    for i in range(cams):
        path_str = abspath(getsourcefile(lambda:0))
        path_split = path_str.rsplit('/', 2)
        stream_info = os.path.join(path_split[0] + "/" + "Data" + "/" + "Results" + "/" + model[i] + "/" + ("stream_info_html.txt"))

        with open(stream_info, 'rb') as stream_data:
            codeclist1 = []
            codeclist2 = []
            aspectratios = []
            resolutionlist1 = []
            resolutionlist2 = []
            codeclist1_pattern = re.compile(r'codeclist1')
            codeclist2_pattern = re.compile(r'codeclist2')
            aspectratios_pattern = re.compile(r'aspectratios')
            resolutionlist1_pattern = re.compile(r'resolutionlist1')
            resolutionlist2_pattern = re.compile(r'resolutionlist2')
            
            for lines in stream_data.readlines():
        	lines = str(lines.strip())
                match1 = codeclist1_pattern.match(lines)
                match2 = codeclist2_pattern.match(lines)
                match3 = aspectratios_pattern.match(lines)
                match4 = resolutionlist1_pattern.match(lines)
                match5 = resolutionlist2_pattern.match(lines)
                if match1:
                    line = lines.split("=", 1)[1]
                    codeclist1 = line.split(",")
                if match2:
                    line = lines.split("=", 1)[1]
                    codeclist2 = line.split(",")
                if match3:
                    line = lines.split("=", 1)[1]
                    aspectratios = line.split(",")
                if match4:
                    line = lines.split("=", 1)[1]
                    resolutionlist1 = line.split(",")
                if match5:
                    line = lines.split("=", 1)[1]
                    resolutionlist2 = line.split(",")

        str_1 = 0
        str_2 = 0
        str_3 = 0
        str_4 = 0

        cam_response = []
        cam_soup = []
        cam_soupbody = []

        url1 = ("http://%s:%s/config/video.cgi?profileid=1&codec=%s&resolution=%s&framerate=30&qualitymode=CBR&bitrate=4096" % (address[i], port[i], codeclist1[0], resolutionlist1[0]))
        url2 = ("http://%s:%s/config/stream_info.cgi" % (address[i], port[i]))
#        response1 = requests.get(url1)
#        response2 = requests.get(url2)

        response1 = requests.get(url1, auth=('admin', 'admin'))
        response2 = requests.get(url2, auth=('admin', 'admin'))
        str1_1 = str(response1)
        str2_1 = str(response2)

#        html1 = response2.text
        if str2_1 == ("<Response [200]>"):
            print (response2.text)
            print (model[i] + "  " + "AV encoder ready")
"""
        # connect
        if str1_1 == ("<Response [401]>"):
            #print ("Wrong password.")
            time.sleep(1)
            url1 = ("http://%s:%s/cgi-bin/setcodec.cgi?videocodec=1&profile1format=%s&profile1resolution=%s&profile1pfs=30&profile1qmode=0&profile1bps=1M" % (address[i], port[i], codeclist1[0], resolutionlist1[0]))
            url2 = ("http://%s:%s/cgi-bin/videocodecready.cgi" % (address[i], port[i]))
            response1 = requests.get(url1, auth=('admin', ''))
            response2 = requests.get(url2, auth=('admin', ''))
            str1_2 = str(response1)
            str2_2 = str(response2)

            html1 = response2.text
            if html1 == ("videocodecready=1"):
                print (model[i] + "AV encoder ready")

        if str1_2 == ("<Response [401]>"):
            #print ("Digest needed.")
            time.sleep(1)
            url1 = ("http://%s:%s/cgi-bin/setcodec.cgi?videocodec=1&profile1format=%s&profile1resolution=%s&profile1pfs=30&profile1qmode=0&profile1bps=1M" % (address[i], port[i], codeclist1[0], resolutionlist1[0]))
            url2 = ("http://%s:%s/cgi-bin/videocodecready.cgi" % (address[i], port[i]))
            response1 = requests.get(url1, auth=('admin', ''))
            response2 = requests.get(url2, auth=('admin', ''))
            str1_3 = str(response1)
            str2_3 = str(response2)

            html1 = response2.text
            if html1 == ("videocodecready=1"):
                print (model[i] + "AV encoder ready")
            
        if str1_3 == ("<Response [401]>"):
            #print  ("Password in digest needed.")
            time.sleep(1)
            url1 = ("http://%s:%s/cgi-bin/setcodec.cgi?videocodec=1&profile1format=%s&profile1resolution=%s&profile1pfs=30&profile1qmode=0&profile1bps=1M" % (address[i], port[i], codeclist1[0], resolutionlist1[0]))
            url2 = ("http://%s:%s/cgi-bin/videocodecready.cgi" % (address[i], port[i]))
            response1 = requests.get(url1, auth=('admin', ''))
            response2 = requests.get(url2, auth=('admin', ''))
            str1_4 = str(response1)
            str2_4 = str(response2)

            html1 = response2.text
            if html1 == ("videocodecready=1"):
                print (model[i] + "AV encoder ready")






"""

#    return (codeclist1, codeclist2, resolutionlist1, resolutionlist2, module_name)
