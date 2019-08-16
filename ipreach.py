import sys
import subprocess

#Tests the reachability of each of the Ip addresses provided.
pingIP = []
def pingTest(ipValid):
    for i in range(len(ipValid)):
        ipValid[i] = ipValid[i].strip("\n")
        ipreply = subprocess.call('ping %s /n 3' %(ipValid[i]), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if(ipreply == 0):
            pingIP.append(ipValid[i])
        else:
            print("IP address %s is unreachable"%ipValid[i])
            
    return pingIP