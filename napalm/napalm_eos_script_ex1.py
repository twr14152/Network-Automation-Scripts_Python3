from napalm import get_network_driver
from pprint import pprint
from getpass import getpass

def main():
    ips = input("Enter the ips of the devices to connect to seperated by spaces\n")
    un = input("Username: ")
    pw = getpass("Password: ")
    ipadd = ips.split()
    for ip in ipadd:
        print("Connecting to EOS Device:", ip)
        driver = get_network_driver("eos")
        sw = driver(ip, un, pw)
        sw.open()
        pprint(sw.get_facts())
        pprint(sw.get_arp_table())
        pprint(sw.get_config())
        pprint(sw.get_environment())
        pprint(sw.get_interfaces_ip())
        pprint(sw.get_lldp_neighbors_detail())

if __name__ == "__main__":
    main()
