#!/usr/bin/python3
#(c) 2018 Todd Riemenschneider
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
        print("Pre-change state", k)
        pre_change01 = net_connect.send_command('show running-config')
        pp(pre_change01)
        print("************************************")
        configs01 = net_connect.send_config_set(v)
        pp(configs01)
        print("++++++++++++++++++++++++++++++++++++")
        print("Post-change state: ", k)
        post_change01 = net_connect.send_command('show running-config')
        pp(post_change01)
    except Exception as cmd_error:
        print("Command not working, make sure syntax is correct")
        print("Problem with commands on: ", k)
        print(cmd_error)
        continue

print('Problems connecting to these hosts: ',  err_host)
