#!/usr/bin/python3
import netmiko
from pprint import pprint as pp

devs_to_cfg = input("Number of devices to configure: " )
count = int(devs_to_cfg)

commands = {}
err_host = []

for i in range(count):
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
        ios_rtr = {
            "device_type": "cisco_ios",
            "ip": k,
            "username": "admin",
            "password": "automate",
        }
        net_connect = netmiko.ConnectHandler(**ios_rtr)
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
        output = net_connect.send_config_set(v)
        pp(output)
        print("Post-change state: ", k)
        output2 = net_connect.send_config_set(['show running-config'])
    except Exception as cmd_error:
        print("Command not working, make sure syntax is correct")
        print("Problem with commands on: ", k)
        print(cmd_error)
        continue

print('Problems connecting to these hosts: ',  err_host)
