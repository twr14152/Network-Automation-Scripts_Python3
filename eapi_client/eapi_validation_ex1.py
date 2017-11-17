import pyeapi
from pprint import pprint as pp

host1 = pyeapi.connect_to("sw1")
host2 = pyeapi.connect_to("sw2")

devices = [host1, host2]

value = 0

for host in devices:
    value += 1
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Current State: ", host)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    pp(host.enable(['show hostname', 'show running-config', 'show ip route', 'show ip ospf neighbor']))
    

