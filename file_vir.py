import os
    
## Extracts ip addresses and stores them in a list    
def extract_ip(ipadd):
  
    ## Verifies that path is reachable
    if os.path.isfile(ipadd) == True:
        # Opens file for reading
        ip_file = open(ipadd, "r")
        
        #starts reading line from begining of character
        ip_file.seek(0)
        
        #Reads ip addresses to a list
        ipList = ip_file.readlines()
        
        #Close file
        ip_file.close()
    
        return ipList
    else:
        print("Enter valid file location!!!")

    
    




