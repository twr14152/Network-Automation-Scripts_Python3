import pyeapi
from pprint import pprint as pp

cmds1 = input('Enter commands for veos1 seperate with ",": ')
cmds2 = input('Enter commands for veos2 seperate with ",": ') 
cmds3 = input('Enter commands for veos3 seperate with ",": ') 

hosts = input('Enter hosts seperated by spaces: ')
devices = hosts.split()
commands1 = cmds1.split(',')
commands2 = cmds2.split(',')
commands3 = cmds3.split(',')

for host in devices:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Pre-change State: ", host)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    node = pyeapi.connect_to(host)
    pp(node.enable(['show running-config']))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Post-Change State:", host)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if host == 'veos1':
        pp(node.config(commands1))
        pp(node.enable(['show running-config']))
    elif host == 'veos2':
        pp(node.config(commands2))
        pp(node.enable(['show running-config']))
    elif host == 'veos3':
        pp(node.config(commands3))
        pp(node.enable(['show running-config']))
       
