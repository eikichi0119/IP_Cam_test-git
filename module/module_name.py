#!/usr/bin/env python
#coding=UTF-8
import inspect

def info():
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    mod_name = str(mod.__name__)
    return mod_name
