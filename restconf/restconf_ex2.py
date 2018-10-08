import requests
import sys
from pprint import pprint as pp

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# use the IP address or hostname of your Cat9300
HOST = 'ios-xe-mgmt.cisco.com:9443'
USER = 'root'
PASS = 'D_Vay!_10&'


# create a main() method
def main():
    """Main method that retrieves the Interface details from Cat9300 via RESTCONF."""

    # url string to issue GET request
    # get interfaces info
    url = "https://{h}/restconf/data/ietf-interfaces:interfaces".format(h=HOST)
    print(url)
    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}
    # this statement performs a GET on the specified url
    # the response variable will store the data in a json format
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, verify=False).json()

    # pretty print is used make reading the json output easier
    pp(response)

if __name__ == '__main__':
    sys.exit(main())
