#This is the telnet Library for Python3
#Make sure transport input telnet is enabled on router validate

from getpass import getpass
import telnetlib

host = input("Enter host IPs u want to connect to seperate using a space : ")
cmd = input("Enter cmd seperate with a ',' : ")
user = input("Username: ")
password = getpass("Password: ")

#create lists to iterate through
hosts = host.split()
cmds = cmd.split(",")

for HOST in hosts:
    print("Connecting to host:", HOST)
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

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
