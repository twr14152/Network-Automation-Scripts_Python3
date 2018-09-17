from ncclient import manager
import xml.dom.minidom


conn = manager.connect(
        host='ios-xe-mgmt.cisco.com',
        port=10000,
        username="root",
        password="D_Vay!_10&",
        hostkey_verify=False,
        device_params={'name': 'default'},
        look_for_keys=False)



hostname_filter = '''
                      <filter>
                          <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                          </native>
                      </filter>
                      '''

       # Pretty print the XML reply
xmlDom = xml.dom.minidom.parseString( str( conn.get_config('running', hostname_filter)))
print(xmlDom.toprettyxml( indent = "  " ))
