import pyeapi
from pprint import pprint as pp

node1 = pyeapi.connect_to('ceos1')
node2 = pyeapi.connect_to('ceos2')

node1.api("ipinterfaces").create("Ethernet1")
node2.api("ipinterfaces").create("Ethernet1")

node1.config("ip name-server 8.8.8.8")
node1.config("ip route 0.0.0.0/0 192.168.1.1")

node2.config("ip name-server 8.8.8.8")
node2.config("ip route 0.0.0.0/0 192.168.1.1")

pp(node1.run_commands("ping cisco.com"))
pp(node2.run_commands("ping cisco.com"))

cmds = ["show version", "show running-config", "show management api http-commands"]

pp(node1.run_commands(cmds))
pp(node2.run_commands(cmds))

configurations1 = [
"hostname ceos1",
"ip routing",
"interface Ethernet1",
"ip address 10.0.0.1/24",
"no shutdown",
"interface loopback 1",
"description router-id",
"ip address 1.1.1.1/32",
"router ospf 1",
"network 10.0.0.0 0.0.0.255 area 0",
"network 1.1.1.1 0.0.0.0 area 0",
"router-id 1.1.1.1",
]

configurations2 = [
"hostname ceos2",
"ip routing",
"interface Ethernet1",
"ip address 10.0.0.2/24",
"no shutdown",
"interface loopback 1",
"description router-id",
"ip address 2.2.2.2/32",
"router ospf 1",
"network 10.0.0.0 0.0.0.255 area 0",
"network 2.2.2.2 0.0.0.0 area 0",
"router-id 2.2.2.2",
]


node1.config(configurations1)
node2.config(configurations2)

pingHost = ["ping 1.1.1.1", "ping 2.2.2.2"]

print("#" * 45)
print("Printing results of ping to loopbacks advertised via ospf")
pp(node1.run_commands(pingHost))
pp(node1.run_commands("show running-config"))

print("#" * 45)
print("Printing results of ping to loopbacks advertised via ospf")
pp(node2.run_commands(pingHost))
pp(node2.run_commands("show running-config"))

