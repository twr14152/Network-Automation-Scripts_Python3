#Simple Eapi test script
import pyeapi
from pprint import pprint as pp

#Connect to the host
host = pyeapi.connect_to("sw1")

#Commands to run
pp(host.enable('show version'))
pp(host.enable('show running-config'))

