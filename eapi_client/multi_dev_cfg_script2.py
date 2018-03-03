#(c) 2017 Todd Riemenschneider

import pyeapi
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
        node = pyeapi.connect_to(k)
        pp(node.enable(['show running-config']))
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
        pp(node.config(v))
        print("Post-change state: ", k)
        pp(node.enable(['show running-config']))
    except Exception as cmd_error:
        print("Command not working, make sure syntax is correct")
        print("Problem with commands on: ", k)
        print(cmd_error)
        continue

print('Problems connecting to these hosts: ',  err_host)
