import os
import file_vir 
import ipaddr_vir
import ipreach
import ssh_func
from ssh_threads import noautoThread
from ssh_func import ssh_conn


#Increments for each network device; used to loop through "ssh_credentials.txt" to extract login details for each network device in the GNS3 net topology.
ctr = 1

#Inputs text file containing IP address into file_vir function to get ip addresses in a list.
ipadd = input("Enter file path to text file containing ip addresses without quotations: ")
ip_list = file_vir.extract_ip(ipadd)

#Verifies that the ip addresses used are valid.
ipValid = ipaddr_vir.ipaddChk(ip_list)

#Tests reachability of each of the ip addresses.
connIP =ipreach.pingTest(ipValid)

#Stores path to SSH login credentials and cmd files in variables.
login_file = input("Enter file path to text file containing login files without quotations: ")
cmd_file = input("Enter file path to text file containing cmd files without quotations: ")

#SSH into multiple routers concurrently using threading.
noautoThread(connIP,cmd_file,login_file,ctr,ssh_conn)