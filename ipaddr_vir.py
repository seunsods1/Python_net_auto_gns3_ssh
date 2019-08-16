import os
import sys

# Check that the ip addresses provided are valid
def ipaddChk(ip_list):
    ip_valid = []
    for i in range(len(ip_list)):
        ip_list[i] = ip_list[i].strip('\n')
    
        #Checks that the right number of "." are used in each of the ip addresses.
        if (ip_list[i].count(".",0,-1) != 3):
            print("Enter Valid IP address",ip_list[i], "is not valid")
        
        else:            
            #Checks that the ip address used is allowed.
            value = ip_list[i].split(".")
                            
            if(((int(value[0])> 0)and(int(value[0])< 224)) and (value[0]!="127")and(value[0]+"."+value[1]!="169.254")):
                ip_valid.append(ip_list[i])
                continue
            else:
                print("Ip address",ip_list[i],"is not allowed")
        
    return ip_valid