#!/usr/bin/python3

import pyeapi
from pprint import pprint as pp

hosts = ['ceos1', 'ceos2', 'ceos3', 'ceos4']

cmds = ["show running-config", 'write memory']


for host in hosts:
    node = pyeapi.connect_to(host)
    pp(node.run_commands(cmds[0]))
    pp(node.run_commands(cmds[1]))
    print("\n\n\n")



