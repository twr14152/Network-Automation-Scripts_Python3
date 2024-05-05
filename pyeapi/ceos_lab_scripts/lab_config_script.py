#!/usr/bin/python3

import pyeapi
from pprint import pprint as pp

ans = input("Are you configuring more than one device? (y or n): ")

if ans == 'y':
    devices = input("Enter device names seperated by ',': ")
    dev_list = devices.split(',')
    cmds = input("Enter config lines separated by ',': ")
    configuration = cmds.split(',')
    for dev in dev_list:
        node = pyeapi.connect_to(dev)
        results = node.config(configuration)
        pp(results)
        pp(node.get_config())
else:
    device = input("Enter device you would like to configure: ")
    config = input("Enter config commands seperate lines with ',': ")
    configuration = config.split(",")
    node1 = pyeapi.connect_to(device)
    results = node1.config(configuration)
    pp(results)
    pp(node1.get_config())

print("End of Script!!")
