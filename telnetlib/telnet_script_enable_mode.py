#This is the telnet Library for Python3
#Make sure transport input telnet is enabled on router validate
#This scripts will run commands you choose on the remote devices using telnet as transport
#The results will be print to screen and captured in files named ("router_" + HOST)
#(c) 2017 Todd Riemenschneider

from getpass import getpass
import telnetlib

user = input("Username: ")
password = getpass("Password: ")
enpw = getpass("Enable: ")

with open('host_file.txt') as f:
    hosts = f.read().splitlines()

commands = '''
show cdp neighbor
show run
show version
show inventory
'''

cmds = commands.splitlines()


for HOST in hosts:
    print("Connecting to host:", HOST)
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"enable \n")
        tn.read_until(b"Password: ")
        tn.write(enpw.encode('ascii') + b"\n")

    tn.write(b"term length 0\n")
    #iterate through cmds using for loop
    for CMD in cmds:
        tn.write(CMD.encode('ascii') + b"\n")
    tn.write(b"exit\n")
    readoutput = tn.read_all().decode('ascii')
    saveoutput =  open("router_" + HOST, "w")
    saveoutput.write(readoutput)
    saveoutput.write("\n")
    saveoutput.close
    #This command will print out the saved output on your screen
    print(readoutput)

