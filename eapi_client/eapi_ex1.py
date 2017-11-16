#Eapi test script
import pyeapi
from pprint import pprint as pp

host1 = pyeapi.connect_to("sw1")
host2 = pyeapi.connect_to("sw2")

devices = [host1, host2]

for host in devices: 
    print(host)
    pp(host.enable('show version'))
    pp(host.enable('show running-config'))
