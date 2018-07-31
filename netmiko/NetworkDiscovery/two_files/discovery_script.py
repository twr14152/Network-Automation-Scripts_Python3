#!/usr/bin/python3
#(c) 2017 Todd Riemenschneider
#
#Enable Multiprocessing
from multiprocessing import Pool
#getpass will not display password
from getpass import getpass
#ConnectionHandler is the function used by netmiko to connect to devices
from netmiko import ConnectHandler
#Time tracker
from time import time

#create variables for username and password
#create variables for configs and hosts
uname = input("Username: ")
passwd = getpass("Password: ")
# Interactively add the hosts
#host = input("Enter the host IPs seperate with space: ")

#This will allow you to just press enter
#This sets default values Not recommanded in any place but a lab
if len(uname) < 1 : uname = "admin"
if len(passwd) < 1 : passwd = "automate"

#This will put hosts and commands entered into list format
#hosts = host.split()
# To manually add hosts to scripts just follow the format below
#hosts = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"]
# use hostfile

with open('host_file.txt') as f:
    hosts = f.read().splitlines()

starting_time = time()

#Each member of the pool of 5 will be run through this function
def run_script(host_ip):
    ios_rtr = {
        "device_type": "cisco_ios",
        "ip": host_ip,
        "username": uname,
        "password": passwd,
        }
    err_host = []
    nl = "\n"
    #connect to the device via ssh
    try: 
        net_connect = ConnectHandler(**ios_rtr)
        host_name = net_connect.find_prompt()
        # This is the first command issued
        output1 = net_connect.send_command('show version', use_textfsm=False)
        print("Connected to host:", host_ip)
        print(output1)
        host_id = "Connected to host: " + host_ip
        print('\n---- Elapsed time=', time()-starting_time)
        # This is the second command issued
        output2 = net_connect.send_command('show cdp nei', use_textfsm=False)
        print("Connected to host:", host_ip)
        print(output2)
        host_id = "Connected to host: " + host_ip
        print('\n---- Elapsed time=', time()-starting_time)
        # This is the third command issued
        output3 = net_connect.send_command('show inventory', use_textfsm=False)
        print("Connected to host:", host_ip)
        print(output3)
        host_id = "Connected to host: " + host_ip
        print('\n---- Elapsed time=', time()-starting_time)
        # This is the fourth command issued
        output4 = net_connect.send_command('show run', use_textfsm=False)
        print("Connected to host:", host_ip)
        print(output4)
        host_id = "Connected to host: " + host_ip
        print('\n---- Elapsed time=', time()-starting_time)
        with open(host_ip + "_discovery_file.txt", 'w') as file:
            file.write(host_id)
            file.write(nl)
            file.write(host_name)
            file.write(nl)
            file.write(output1)
            file.write(nl)
            file.write(host_id)
            file.write(nl)
            file.write(host_name)
            file.write(nl)
            file.write(output2)
            file.write(nl)
            file.write(host_id)
            file.write(nl)
            file.write(host_name)
            file.write(nl)
            file.write(output3)
            file.write(nl)
            file.write(host_id)
            file.write(nl)
            file.write(host_name)
            file.write(nl)
            file.write(output4)
            file.write(nl)
    except Exception as unknown_error:
        # Error handling - Print output to screen
        print("************************************")
        print("Unable to log into this device:", host_ip)
        print(unknown_error)
        print("************************************")
        # Error handling - record to file
        with open("Connection_Errors", "a") as err_log:
            err_log.write("Error connecting to the following devices")
            err_log.write(nl)
            err_log.write(str(unknown_error))
            err_log.write(nl)
            err_log.write(host_ip)
            err_log.write(nl)


if __name__ == "__main__":
    # Pool(5) means 5 process will be run at a time, more hosts will go in the next group
    with Pool(5) as p:
        print(p.map(run_script, hosts))
