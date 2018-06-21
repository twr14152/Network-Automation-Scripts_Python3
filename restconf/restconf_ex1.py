# This is an example of restconf script hitting cisco devnet lab device (CSR1000V)

import requests

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# login creds
HOST  = "ios-xe-mgmt.cisco.com:9443"
USER = 'root'
PASS = 'D_Vay!_10&'

# create a main() method
def main():
    """Main method that retrieves info from the device using RESTCONF."""
    # Still trying to work through understanding yang models
    # url string to issue GET request
    #url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=HOST)
    #url = "https://{h}/restconf/data/Cisco-IOS-XE-native:native/interface?".format(h=HOST)
    # running config
    #url = "https://{h}/restconf//data/Cisco-IOS-XE-native:native?content=config&depth=65535".format(h=HOST)
    # Pull a bunch of yang modules + descriptions
    url = "https://{h}/restconf/data?fields=ietf-yang-library:modules-state/module".format(h=HOST)
    # Pull the vlans
    #url = "https://{h}/restconf/tailf/modules/Cisco-IOS-XE-vlan/2017-10-02".format(h=HOST)
    # Same as above - Pull a bunch of yang modules + descriptions
    #url = "https://{h}/restconf/data?fields=ietf-yang-library:modules-state/module(name;revision;schema;namespace)".format(h=HOST)
    #url = "https://{h}/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities".format(h=HOST) 
    # Just an example of scheme found in yang modules + descriptions
    #url = "https://{h}/restconf/tailf/modules/openconfig-network-instance-l3/2017-01-13".format(h=HOST)    


    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False)

    # print the json that is returned
    print(response.text)

if __name__ == '__main__':
    main()
