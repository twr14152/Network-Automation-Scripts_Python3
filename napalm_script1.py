
from napalm_base import get_network_driver
import napalm_ios
from pprint import pprint

def main():
#   Uncomment the line below for python2
#    ips = raw_input("Routers to run through: ")
#   Uncomment the line below for python3
    ips = input("Routers to run through (Use a space between each router): ")
    ipadd = ips.split()
    for ip in ipadd:
        print("connecting to router", ip)
        driver = get_network_driver('ios')
        rtr = driver(ip, 'automate', 'automation') 
        rtr.open()
        #ios_output = rtr.get_config()
        pprint(rtr.get_config())
        interfaces = rtr.get_interfaces()
        pprint(interfaces)
        pprint(rtr.get_facts())


if __name__ == "__main__":
    main()

