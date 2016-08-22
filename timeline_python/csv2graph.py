#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import re, pylab
import pandas as pd
from matplotlib import font_manager, rc

ip_for_Domain = {}
ip_for_Auth_Protocol = {}
ip_for_Destination = {}
ip_for_Logon_Type = {}
ip_for_User = {}
ip_for_Date_Time = {}
ip_for_Log_File = {}
ip_for_Type = {}
ip_for_Event_ID = {}
ip = []

f = open("logons_redacted_fixed20160520_fakeIP.csv", "rb")

line = f.readline()

while True:
    line = f.readline().split(",")
    if not line: break
    if len(line) == 1:
        break
    ip = re.findall("([0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]+)",line[4])
    if(len(ip) == 0):
        ip.append("127.0.0.1")
    if ip[0] not in ip_for_User.keys():
        ip_for_Domain[ip[0]] = [line[0]]
        ip_for_Auth_Protocol[ip[0]] = [line[1]]
        ip_for_Destination[ip[0]] = [line[2]]
        ip_for_Logon_Type[ip[0]] = [line[3]]
        if line[5] == "":   
            ip_for_User[ip[0]] = ["NTLM"]
        else:
            ip_for_User[ip[0]] = [line[5]]
        if line[6][-2:] == 'PM' or line[6][-2:] == 'AM':
            ip_for_Date_Time[ip[0]] = [pd.to_datetime(line[6], format='%m/%d/%Y %I:%M:%S %p')]
        else:
            ip_for_Date_Time[ip[0]] = [pd.to_datetime(line[6], format='%d/%m/%Y %H:%M:%S')]
        ip_for_Log_File[ip[0]] = [line[7]]
        ip_for_Type[ip[0]] = [line[8]]
        ip_for_Event_ID[ip[0]] = [line[9]]
    else:
        ip_for_Domain[ip[0]].append(line[0])
        ip_for_Auth_Protocol[ip[0]].append(line[1])
        ip_for_Destination[ip[0]].append(line[2])
        ip_for_Logon_Type[ip[0]].append(line[3])
        if line[5] == "":   
            ip_for_User[ip[0]].append("NTLM")
        else:
            ip_for_User[ip[0]].append(line[5])                                         
            
        if line[6][-2:] == 'PM' or line[6][-2:] == 'AM':
            ip_for_Date_Time[ip[0]].append(pd.to_datetime(line[6], format='%m/%d/%Y %I:%M:%S %p'))
        else:
            ip_for_Date_Time[ip[0]].append(pd.to_datetime(line[6], format='%d/%m/%Y %H:%M:%S'))
        ip_for_Log_File[ip[0]].append(line[7])
        ip_for_Type[ip[0]].append(line[8])
        ip_for_Event_ID[ip[0]].append(line[9])
  


    
f.close()

ip_list = list(ip_for_User.keys())

for i in range(len(ip_list)):
    fig = plt.figure(figsize=(25, 15))
    ax = fig.add_subplot(111)
    x = range(len(ip_for_User[ip_list[i]]))
    plt.xticks(x, ip_for_User[ip_list[i]], rotation = 90)
    plt.plot(x, ip_for_Date_Time[ip_list[i]],'bo')
    plt.title(ip_list[i])
    #plt.gcf().autofmt_xdate()

    #plt.show()
    fig.savefig(ip_list[i] + ".png")
    plt.close()