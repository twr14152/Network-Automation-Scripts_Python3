#!/usr/bin/python3
#(c) 2020 Todd Riemenschneider
# 
"""
Wrote this script based off of a request I got:

I am looking script which will run below command and provide output
Conf t
ip http client connection forceclose
end
sh ip http client all

this I want to run on multiple IP and want to create an output file for all file can I use script shown
"""
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

#This will allow you to just press enter
#This sets default values Not recommanded in any place but a lab
if len(uname) < 1 : uname = "developer"
if len(passwd) < 1 : passwd = "C1sco12345"


# Pull target hosts from host_file
with open('host_file.txt') as f:
    hosts = f.read().splitlines()

config_cmd = ["ip http client connection forceclose",]


commands = 'show ip http client all'

starting_time = time()

#Each member of the pool of 5 will be run through this function
def run_script(host_ip):
    ios_rtr = {
        "device_type": "cisco_ios",
        "host": host_ip,
        "port": 8181,
        "username": uname,
        "password": passwd,
        }
    nl = "\n"
    try: 
        #Connect to the device via ssh
        net_connect = ConnectHandler(**ios_rtr)
        host_name = net_connect.find_prompt()
        print("Connected to host:", host_ip)
        host_id = "Connected to host: " + host_ip
        print('\n---- Elapsed time=', time()-starting_time)
        cmd_output = net_connect.send_command(commands)
        print(f"Pre-config state:{cmd_output}")
        cfg_output = net_connect.send_config_set(config_cmd)
        print(f"Config:{cmd_output}")
        cmd_output2 = net_connect.send_command(commands)
        print(f"Post-config state:{cmd_output2}")
        print(cfg_output)
        with open(host_ip + "_.txt", 'a') as file:
            file.write(host_id)
            file.write(nl)
            file.write(host_name)
            file.write(nl)
            file.write(cmd_output)
            file.write(nl)
            file.write(str(config_cmd))
            file.write(nl)
            file.write(cfg_output)
            file.write(nl)
            file.write(cmd_output2)
            file.write(nl)
            file.write("**************************************")
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


