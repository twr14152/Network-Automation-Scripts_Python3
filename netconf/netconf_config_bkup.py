from ncclient import manager
import xml.dom.minidom

HOSTS = ['ios-xe-mgmt-latest.cisco.com', 'ios-xe-mgmt.cisco.com']
PORT = 10000
USER = 'developer'
PASS = 'C1sco12345'


def main():
    for HOST in HOSTS:
        with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         look_for_keys=False, allow_agent=False) as m:
            print(HOST, "- running-config copied ")
            config = m.get_config('running')
            xml_data = xml.dom.minidom.parseString(config.xml)
            router_configs = xml_data.toprettyxml(indent = "  ")
            #print(router_configs)
            with open("config_bkups/" + HOST + "_running_config.txt", 'w') as file:
                file.write(router_configs)
 

if __name__ == "__main__":
    main()
