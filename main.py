#!/usrbin/env python
#coding=UTF-8

import module.FindZeroconfServiceTypes as FS
import module.WriteFile as WF
import module.ServiceBrowser as SB
import module.version_htm as VH
import module.info as ifo
import module.sensor_info as SI
import module.sensor as SR
import module.stream_info as SIFO
import os
import errno
from inspect import getsourcefile
from os.path import abspath
import module.stream_get_resolution as GR

str_GetServ, mod_GetServ = FS.get_service()
WF.write_file(str_GetServ, mod_GetServ, 0, 0)

SB.service_browser(mod_GetServ)

cams, model, address, port, str_GetVerRespon, str_GetVerHTML, str_GetVerHTMLBody, mod_GetVer = VH.version_htm()
for i in range(cams):
    WF.write_file(str_GetVerRespon[i], (mod_GetVer + "_response"), model[i], 1)
    WF.write_file(str_GetVerHTML[i], (mod_GetVer + "_html"), model[i], 1)
    WF.write_file(str_GetVerHTMLBody[i], (mod_GetVer + "_html_body"), model[i], 1)

cams, model, address, port, str_GetInfoRespon, str_GetInfoHTML, str_GetInfoHTMLBody, mod_GetInfo = ifo.info()
for i in range(cams):
    WF.write_file(str_GetInfoRespon[i], (mod_GetInfo + "_response"), model[i], 1)
    WF.write_file(str_GetInfoHTML[i], (mod_GetInfo + "_html"), model[i], 1)
    WF.write_file(str_GetInfoHTMLBody[i], (mod_GetInfo + "_html_body"), model[i], 1)

cams, model, address, port, str_GetSenInfoRespon, str_GetSenInfoHTML, str_GetSenInfoHTMLBody, mod_GetSenInfo = SI.sensor_info()
for i in range(cams):
    WF.write_file(str_GetSenInfoRespon[i], (mod_GetSenInfo + "_response"), model[i], 1)
    WF.write_file(str_GetSenInfoHTML[i], (mod_GetSenInfo + "_html"), model[i], 1)
    WF.write_file(str_GetSenInfoHTMLBody[i], (mod_GetSenInfo + "_html_body"), model[i], 1)

cams, model, address, port, str_GetSenRespon, str_GetSenHTML, str_GetSenHTMLBody, mod_GetSen = SR.sensor()
for i in range(cams):
    WF.write_file(str_GetSenRespon[i], (mod_GetSen + "_response"), model[i], 1)
    WF.write_file(str_GetSenHTML[i], (mod_GetSen + "_html"), model[i], 1)
    WF.write_file(str_GetSenHTMLBody[i], (mod_GetSen + "_html_body"), model[i], 1)

cams, model, address, port, str_GetStreamInfoRespon, str_GetStreamInfoHTML, str_GetStreamInfoHTMLBody, mod_GetStreamInfo = SIFO.stream_info()
for i in range(cams):
    WF.write_file(str_GetStreamInfoRespon[i], (mod_GetStreamInfo + "_response"), model[i], 1)
    WF.write_file(str_GetStreamInfoHTML[i], (mod_GetStreamInfo + "_html"), model[i], 1)
    WF.write_file(str_GetStreamInfoHTMLBody[i], (mod_GetStreamInfo + "_html_body"), model[i], 1)

GR.get_resolution(cams, model, address, port)
#codeclist1, codeclist2, resolutionlist1, resolutionlist2, mod_GetResolution = GR.get_resolution(cams, model, address, port)
#print (codeclist1)
#print (codeclist2)
#print (resolutionlist1)
#print (resolutionlist2)
