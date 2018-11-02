import pyeapi
from pprint import pprint as pp

node1 = pyeapi.connect_to('ceos1')
node2 = pyeapi.connect_to('ceos2')

cmds = ["show version", "show ip route", "show ip ospf neighbor"]

pp(node1.run_commands(cmds))
pp(node2.run_commands(cmds))
