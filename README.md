TITLE:
#Python_net_auto_gns3_ssh

OBJECTIVES:
This project demonstrates how python can be used to automate the configuration of various network devices concurrently in a live network by automating a couple network devices in gns3.

TOOLS USED:
software - Gns3, Programming Language - Python 3.7.2, Key Python Libraries - Paramiko, Threading, Subprocess, and Time.

Procedure:
1) Setup network topology on gns3, that will consist of two routers connected to two hosts (VPCs) and the internet and manage networks with a local PC by adding it to the rest of the topology.
2) Write python code on local pc to enable a user input, a text file containing a list of ip addresses, an ssh login credential file containing the credentials necessary to login into the network devices, and a command file consisting of the commands to be executed on the network devices in the topology.
   .) The python code should verify the format of the ip addresses provided in the text containing the list of ip addresses.
   .) The python code should verify the destination path to all the text files inputted. 
   .) The python code should include threading to allow multiple network devices to be accessed conurently.
   .) Lastly, python code should be executed on windows command line.
   
Result:
The python code was succesfully able to ssh into the routers in the network topology on gns3 and execute the command "show ip int brief" for both routers concurrently. The python code also extracted the relevant data from a bunch of raw text of the "show ip int brief" and ouputed the result on windows command line.

Aknowledgements:
This project was inspired by a course on UDEMY titled: "Python 3 Network Programming - Build 5 Network Applications by Mihai Catalin.

References:
https://www.udemy.com/python-programming-for-real-life-networking-use
