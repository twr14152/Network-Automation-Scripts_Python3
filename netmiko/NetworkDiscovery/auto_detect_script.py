# This script will go out and detect the device_type for any devices supported by netmiko
# (c) 2018 Todd Riemenschneider

from multiprocessing import Pool
from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_dispatcher import ConnectHandler
from getpass import getpass

uname = input("Username: ")
passwd = getpass("Password: ")

if len(uname) < 1 : uname = "admin"
if len(passwd) < 1 : passwd = "automate"


with open('host_file.txt') as f:
    hosts = f.read().splitlines()


#for host in hosts:
def run_script(host_ip):
    remote_device = {"device_type":"autodetect",
                     "host": host_ip,
                     "username": "admin",
                     "password": "automate"
                     }
    try:
        guesser = SSHDetect(**remote_device)
        best_match = guesser.autodetect()
        print(best_match + " is the device_type for " + host_ip)
    except:
        print("Error connecting to " + host_ip)
        pass

if __name__ == "__main__":
    # Pool(5) means 5 process will be run at a time, more hosts will go in the next group
    with Pool(5) as p:
        print(p.map(run_script, hosts))

