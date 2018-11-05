import pyeapi
from pprint import pprint as pp

node1 = pyeapi.connect_to('ceos1')
node2 = pyeapi.connect_to('ceos2')

node1.api("ipinterfaces").create("Ethernet1")
node2.api("ipinterfaces").create("Ethernet1")

node1.config("ip name-server 8.8.8.8")
node1.config("ip domain lookup source-interface loopback1")

node2.config("ip name-server 8.8.8.8")
node2.config("ip domain lookup source-interface loopback1")

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
"management telnet",
"no shutdown",
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
"management telnet",
"no shutdown",
]


node1.config(configurations1)
node2.config(configurations2)

pingHost = ["ping 1.1.1.1", "ping 2.2.2.2"]

print("#" * 45)
print("Printing results of ping to loopbacks advertised via ospf")
pp(node1.run_commands(pingHost))

print("Running-Config ceos1")
pp(node1.get_config())

print("#" * 45)
print("Printing results of ping to loopbacks advertised via ospf")
pp(node2.run_commands(pingHost))

print("Running-Config ceos2")
pp(node2.get_config())

pp(node1.run_commands("ping 8.8.8.8"))
pp(node2.run_commands("ping 8.8.8.8"))

