#!/usr/bin/python3
# -----------------------------
# (c) 2020 Todd Riemenschneider
# -----------------------------
# This script is prompting user to determine if they plan on configuring the devices or gathering info using show commands.
# Script tries to be a one stop shop for lab use. 
# Its soo painfully slow may end up ditching it or adding MP processing.
# 
import netmiko
from pprint import pprint as pp

type_of_interaction = input("Is this going to be a config or show command? (Type config or show): ")
devs_to_cfg = input("Number of devices you going to access: " )
count = int(devs_to_cfg)

commands = {}
err_host = []

for i in range(count):
#    ports = input("Enter Port to connect with:" )
#    port = int(ports)
    hosts = input("Enter host device: ")
    cmds = input('Enter commands for device seperate with ",": ') 
    cmd_items = cmds.split(',')
    print(cmd_items)
    commands[hosts]= cmd_items
    print("")
    print("")

print(""" This is the dictionary before the loop""", commands)

for k,v  in commands.items():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Pre-change State: ", k)
    try:
        rtr = {
            "device_type": "cisco_xe",
            "ip": k,
            "username": "developer",
            "password": "C1sco12345",
            "port": 8181,
            "verbose": True,
        }
        net_connect = netmiko.ConnectHandler(**rtr)
        print(net_connect.enable())
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    except Exception as unknown_error:
        print("************************************")
        print("Unable to log into this device:", k)
        print(unknown_error)
        err_host.append(k)
        print("Errors logging into:", err_host)
        print("************************************")
        continue
    try:
        #Remove comments (#) if you want to compare pre and post change   
#        print("Pre-change state", k)
#        pre_change01 = net_connect.send_command('show running-config')
#        pp(pre_change01)
        print(v)
        print("************************************")
        if type_of_interaction.strip() == "config":
            configs01 = net_connect.send_config_set(v)
        else:
            for cmd in cmd_items:
                print("Command:", cmd,"\n",  net_connect.send_command(cmd))
        print(configs01)
        print("++++++++++++++++++++++++++++++++++++")
        print("Post-change state: ", k)
        post_change01 = net_connect.send_command('show running-config')
#        pp(post_change01)
    except Exception as cmd_error:
        print("Command not working, make sure syntax is correct")
        print("Problem with commands on: ", k)
        print(cmd_error)
        continue

print('Problems connecting to these hosts: ',  err_host)
