#!/usr/bin/python3
#(c) 2018 Todd Riemenschneider
import netmiko
from pprint import pprint as pp

# This will enter the number of devices as a string
devs_to_cfg = input("Number of devices to configure: " )
# This will turn the string into an integer
count = int(devs_to_cfg)

# create empty dictionary to be used with the list of commands
commands = {}
# create empty list that will be used to keep track problem hosts
err_host = []

# This will be used to determine how many devices to log into
for i in range(count):
    # Create list of hosts will be in string format
    hosts = input("Enter host device: ")
    # Create list of commands will be in string format
    cmds = input('Enter commands for device seperate with ",": ')
    # Put commands in list format
    cmd_items = cmds.split(',')
    # Sanity check on commands printed to screen
    print(cmd_items)
    # Add to empty dictionary hosts are keys commands are values
    commands[hosts]= cmd_items
    print("")
    print("")

print(""" This is the dictionary before the loop""", commands)

# k = hosts v = commands
for k,v  in commands.items():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Pre-change State: ", k)
    try:
        ios_rtr = {
            "device_type": "cisco_ios",
            "ip": k,
            "username": "admin",
            "password": "automate",
        }
        # Used to connect to hosts using parameters in ios_rtr dictionary
        net_connect = netmiko.ConnectHandler(**ios_rtr)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    except Exception as unknown_error:
        # Error handling - connecting to hosts
        print("************************************")
        print("Unable to log into this device:", k)
        print(unknown_error)
        err_host.append(k)
        print("Errors logging into:", err_host)
        print("************************************")
        continue
    try:
        # This can be used for pre-change status check (turn off with #)
        print("Pre-change state", k)
        pre_change01 = net_connect.send_command('show running-config')
        pp(pre_change01)
        print("************************************")
        configs01 = net_connect.send_config_set(v)
        pp(configs01)
        print("++++++++++++++++++++++++++++++++++++")
        # This can be used for post-change status check (turn off with #)
        print("Post-change state: ", k)
        post_change01 = net_connect.send_command('show running-config')
        pp(post_change01)
    except Exception as cmd_error:
        # Error handling - command syntax issues
        print("Command not working, make sure syntax is correct")
        print("Problem with commands on: ", k)
        print(cmd_error)
        continue

print('Problems connecting to these hosts: ',  err_host)
