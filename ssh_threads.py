import os
import threading

#SSH and executes commands on each network device concurrently.
def noautoThread(connIP,cmd_file,login_file,ctr,ssh_conn):
    
    threads = []
    
    for ip_add in connIP:
        thIP = threading.Thread(target = ssh_conn,args = (ip_add,cmd_file,login_file,ctr))
        thIP.start()
        threads.append(thIP)
        ctr +=1
    for thIP in threads:
        thIP.join()
    
    
    

