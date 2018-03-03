#!/usr/bin/python3
# --------------------------------------------------------------
# (c) 2018 Todd Riemenschneider
# This script will run through all hosts in the host_file
# --------------------------------------------------------------
from getpass import getpass
from netmiko import ConnectHandler
from multiprocessing import Pool
from time import time

# Login info
username = input('Enter username: ')
password = getpass('Enter password: ')

# Useful in a lab setting not production
if len(username) < 1 : username = "admin"
if len(password) < 1 : password = "automate"

# Target hosts
with open('host_file') as f:
    host_file = f.read().splitlines()

show_commands = "show ip route"
err_host = []

print("----The devices being configured----")
print(host_file)

starting_time = time()

# Updated /etc/hosts to use host names rather than host ips

def run_script(hostname):
    print ('Connecting to device: ' + hostname)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': hostname,
        'username': username,
        'password': password
    }
    try:
        net_connect = ConnectHandler(**ios_device)
    except Exception as unknown_error:
        print("************************************")
        print("Unable to log into this device:", hostname)
        print(unknown_error)
        err_host.append(hostname)
        print("Errors logging into:", err_host)        
        print("************************************")
        pass

    try:
        output = net_connect.send_command(show_commands)
        print("++++++++++++++++++++++++++++++++++++++++")
        print("Connected to host: ", hostname)
        print("Command issued:",show_commands)
        print("++++++++++++++++++++++++++++++++++++++++")
        print(output)
        print("++++++++++++++++++++++++++++++++++++++++")
        print("End of configs for device", hostname)
        print("****************************************")
    except Exception as unknown_error:
        pass
    print("Errors logging into:" , err_host)
    # Used to determine how long it takes for the script to run/complete 
    print('\n---- Elapsed time=', time()-starting_time)
    
#Used to set up MP Pools to increase performance
#Specify number of process in the pool to run at same time
#There is no recommendation really trial error as to the right number 
if __name__ == "__main__":
    with Pool(5) as p:
        print(p.map(run_script, host_file))

