from ncclient import manager
import xml.dom.minidom

USER = 'developer'
PASS = 'C1sco12345'

  
    
def connect(host_ip, portnum, user, pwd):
    with manager.connect(host=host_ip, port=portnum, username=user,
            password=pwd, hostkey_verify=False,
            device_params={'name': 'default'},
            look_for_keys=False, allow_agent=False) as m:
        print(host_ip, "- running-config copied ")
        config = m.get_config('running')
        xml_data = xml.dom.minidom.parseString(config.xml)
        router_configs = xml_data.toprettyxml(indent = "  ")
        #print(router_configs)
        with open("config_bkups/" + host_ip + "_running_config.txt", 'w') as file:
            file.write(router_configs)
 

def main():
    connect('sandbox-iosxe-latest-1.cisco.com', 830, USER, PASS)
    connect('ios-xe-mgmt.cisco.com', 10000, USER, PASS)


if __name__ == "__main__":
    main()



'''
i@RaspPi4:~/Coding/Python_folder/netOps/netconf $ cd config_bkups  
pi@RaspPi4:~/Coding/Python_folder/netOps/netconf/config_bkups $ ls -l
total 0
pi@RaspPi4:~/Coding/Python_folder/netOps/netconf/config_bkups $ cd ..
pi@RaspPi4:~/Coding/Python_folder/netOps/netconf $ python3 netconf_iosxe_cfg_bkup.py 
sandbox-iosxe-latest-1.cisco.com - running-config copied 
ios-xe-mgmt.cisco.com - running-config copied 
pi@RaspPi4:~/Coding/Python_folder/netOps/netconf $ ls -l config_bkups/
total 64
-rw-r--r-- 1 pi pi 17861 Jan 25 19:47 ios-xe-mgmt.cisco.com_running_config.txt
-rw-r--r-- 1 pi pi 42620 Jan 25 19:47 sandbox-iosxe-latest-1.cisco.com_running_config.txt
pi@RaspPi4:~/Coding/Python_folder/netOps/netconf $ 

'''
