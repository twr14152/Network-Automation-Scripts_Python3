from ncclient import manager


config_data = '''
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>70</name>
 <description>netconf is a whole lot of work to config an interface!!!!</description>
 <ip>
 <address>
 <primary>
 <address>1.1.1.70</address>
 <mask>255.255.255.255</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
 </native>
</config>
'''
HOST = 'ios-xe-mgmt-latest.cisco.com'
PORT = 10000
USER = 'developer'
PASS = 'C1sco12345'

def main():
    with manager.connect(host=HOST,
                    port = PORT,
                    username = USER,
                    password = PASS,
                    hostkey_verify=False,
                    device_params={'name':'default'}) as m:
        
        print("This is the config to send", config_data)

        netconf_reply = m.edit_config(config_data, target="running")

        print(netconf_reply)

if __name__ == "__main__":
    main()
