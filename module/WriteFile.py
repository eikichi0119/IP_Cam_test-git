#!/usr/bin/env python
#coding=UTF-8

import os
import errno
from inspect import getsourcefile
from os.path import abspath

def write_file(str, module_name, model_name, code):
    if code == 0:
        path_str = abspath(getsourcefile(lambda:0))
        path_split = path_str.rsplit('/', 2)
        # See if 'Essential file' folder exists
        file_name = path_split[0] + "/" + "Data" + "/" + "Essen_files" + "/" + ("%s.txt" % module_name)
        if not os.path.exists(os.path.dirname(file_name)):
            try:
                os.makedirs(os.path.dirname(file_name))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        # Open a file
        with open(file_name, "wb") as f:
            f.write(str)
            f.write('\n')
    if code == 1:
        path_str = abspath(getsourcefile(lambda:0))
        path_split = path_str.rsplit('/', 2)    
        # See if 'Essential file' folder exists
        file_name = path_split[0] + "/" + "Data" + "/" + "Results" + "/" + model_name + "/" + ("%s.txt" % module_name)
        if not os.path.exists(os.path.dirname(file_name)):
            try:
                os.makedirs(os.path.dirname(file_name))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        # Open a file
        with open(file_name, "wb") as f:
            f.write(str)
            f.write('\n')
