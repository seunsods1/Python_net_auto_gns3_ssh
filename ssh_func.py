import os
import sys
import paramiko
import time
import re

#Sets up an ssh connection with a network device in gns3
def ssh_conn(connIP,cmd_file,login_file,ctr):
    
    try:
       
        #Verifies the path to the SSH credentials and command files provided.
        if ((os.path.isfile(login_file)== True) and (os.path.isfile(cmd_file)== True)):
            
            #Opens the file containing SSH login credentials and extracts username and password.
            cred = open(login_file, 'r')
            cred.seek(0)
            
            #Determines where to start extracting the creditials from the "ssh_credentials.txt" file for the different network devices in the topology e.g start at R1 for router 1.
            ind = cred.readlines().index("R"+str(ctr)+"\n")
            cred.seek(0)
            
            #Extracts name and password
            name = cred.readlines()[ind+1].strip('\n').split(':')[1].strip()
            cred.seek(0)
            passwd = cred.readlines()[ind+2].strip('\n').split(':')[1].strip()
            
            #Extracts enable secret from "ssh_credentials.txt" file
            cred.seek(0)
            secret = cred.readlines()[ind+3].strip('\n').split(':')[1].strip()
            
            #Closes file "ssh_credentials.txt" file
            cred.close()
            
            #Starts Session               
            sess = paramiko.SSHClient()
            
            #Auto accepts unknown host keys
            sess.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            #Connects to router using the SSH creds gotten from "ssh_credentials.txt" file
            sess.connect(connIP.strip('\n'), username = name, password = passwd)
            
            #Enters cmd line
            conn = sess.invoke_shell()
            
            #Sets full terminal length for output
            conn.send("enable\n")
            time.sleep(1)
            
            #Inputs enable secret
            conn.send(secret.strip() + "\n")
            time.sleep(4)
            
            #Sets terminal length
            conn.send("terminal length 0\n")
            time.sleep(5)
            
            #Executes commands from cmd file
            cmdfil = open(cmd_file,'r')
            cmdfil.seek(0)
            for line in cmdfil.readlines():
                conn.send(line + '\n')
                time.sleep(25)
            cmdfil.close()            
                     
            #Sets max number of bytes of output 
            r_out = conn.recv(65535)
            
            #Returns the result of "Show ip interface brief" executed on individual routers in gns3
            rout = r_out.decode('ascii')          
            outLst = rout[(rout.index("Protocol\r\n")):].strip("Protocol").split("\r\n")
            outLst = outLst[1:]
                      
            #Extracts the header in "Show ip int brief"
            outLstH = rout[(rout.index("\r\nInterface")):].split("\r\n")[1]
            
            #Creats a new list to store the outputs of "show ip int brief" after all the slicing.
            newoutLst = []
            
            #Appends header to "newoutLst"
            newoutLst.append(outLstH)
            
            #Stores only "Show ip int values" in "up" state in 'newoutLst' list.
            for lst in range((len(outLst))-1):
                if('up' in outLst[lst]):
                    newoutLst.append(outLst[lst])       
            
            #Prints values in newoutLst
            print("\r\nIP Interface states for {}:\n".format("R"+str(ctr)))
            for lst in newoutLst:
                print(lst)           
                
            #Searches for IOS syntax errors and returns message to administrator
            if re.search(b'% Invalid input', r_out):
                print("Error(s) found on device with {}".format(connIP))
            else:
                print("Congrats device with {} completed with no errors".format(connIP))
            
            #Closes session
            sess.close()   
        
        # If SSH login file path provided is invalid exit and send error message to administrator.
        elif (os.path.isfile(login_file) == False):
            print("Enter a valid path; %s is invalid" %login_file)
            sys.exit()
        
        # If command file path provided is invalid exit and send error message to administrator.
        elif (os.path.isfile(cmd_file) == False):
            print("Enter a valid path; %s is invalid" %cmd_file)
            sys.exit()   
       
    except paramiko.AuthenticationException:
        print("Invalid Credentials.\n","Try again\n")