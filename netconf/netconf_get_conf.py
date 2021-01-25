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

'''
python3 netconf_get_config.py 

<?xml version="1.0" ?>
<rpc-reply message-id="urn:uuid:d36065b5-b332-40d0-8edd-d0c4e5dc8f3e" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <data>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <version>16.9</version>
      <boot-start-marker/>
      <boot-end-marker/>
      <banner>
        <motd>
          <banner>^C</banner>
        </motd>
      </banner>
      <service>
        <timestamps>
          <debug>
            <datetime>
              <msec/>
            </datetime>
          </debug>
          <log>
            <datetime>
              <msec/>
            </datetime>
          </log>
        </timestamps>
      </service>
      <platform>
        <console xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
          <output>virtual</output>
        </console>
      </platform>
      <hostname>csr1000v</hostname>
      <enable>
        <secret>
          <type>5</type>
          <secret>$1$gkJ1$EofN9ajW9k18SoRTgkhYr/</secret>
        </secret>
      </enable>
      <username>
        <name>cisco</name>
        <privilege>15</privilege>
        <secret>
          <encryption>5</encryption>
          <secret>$1$aO1Y$0AFVz00ON.hE4WkY.BeYq.</secret>
        </secret>
      </username>
      <username>
        <name>developer</name>
        <privilege>15</privilege>
        <secret>
          <encryption>5</encryption>
          <secret>$1$HtLC$7Kj3hGBoDnSHzdEeR/2ix.</secret>
        </secret>
      </username>
      <username>
        <name>root</name>
        <privilege>15</privilege>
        <secret>
          <encryption>5</encryption>
          <secret>$1$vpY7$mh9d69ui3koSaITBi8k9D/</secret>
        </secret>
      </username>
      <ip>
        <domain>
          <name>abc.inc</name>
        </domain>
        <forward-protocol>
          <protocol>nd</protocol>
        </forward-protocol>
        <route>
          <ip-route-interface-forwarding-list>
            <prefix>0.0.0.0</prefix>
            <mask>0.0.0.0</mask>
            <fwd-list>
              <fwd>GigabitEthernet1</fwd>
              <interface-next-hop>
                <ip-address>10.10.20.254</ip-address>
              </interface-next-hop>
            </fwd-list>
          </ip-route-interface-forwarding-list>
        </route>
        <scp>
          <server>
            <enable/>
          </server>
        </scp>
        <ssh>
          <rsa>
            <keypair-name>ssh-key</keypair-name>
          </rsa>
          <version>2</version>
        </ssh>
        <http xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-http">
          <authentication>
            <local/>
          </authentication>
          <server>true</server>
          <secure-server>true</secure-server>
        </http>
      </ip>
      <interface>
        <GigabitEthernet>
          <name>1</name>
          <description>MANAGEMENT INTERFACE - DON'T TOUCH ME</description>
          <ip>
            <address>
              <primary>
                <address>10.10.20.48</address>
                <mask>255.255.255.0</mask>
              </primary>
            </address>
          </ip>
          <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
          </mop>
          <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
          </negotiation>
        </GigabitEthernet>
        <GigabitEthernet>
          <name>2</name>
          <description>Network Interface</description>
          <shutdown/>
          <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
          </mop>
          <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
          </negotiation>
        </GigabitEthernet>
        <GigabitEthernet>
          <name>3</name>
          <description>Network Interface</description>
          <shutdown/>
          <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
          </mop>
          <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
          </negotiation>
        </GigabitEthernet>
      </interface>
      <control-plane/>
      <login>
        <on-success>
          <log/>
        </on-success>
      </login>
      <multilink>
        <bundle-name xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ppp">authenticated</bundle-name>
      </multilink>
      <redundancy/>
      <spanning-tree>
        <extend xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-spanning-tree">
          <system-id/>
        </extend>
      </spanning-tree>
      <subscriber>
        <templating/>
      </subscriber>
      <crypto>
        <pki xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-crypto">
          <trustpoint>
            <id>TP-self-signed-1530096085</id>
            <enrollment>
              <selfsigned/>
            </enrollment>
            <revocation-check>none</revocation-check>
            <rsakeypair>
              <key-label>TP-self-signed-1530096085</key-label>
            </rsakeypair>
            <subject-name>cn=IOS-Self-Signed-Certificate-1530096085</subject-name>
          </trustpoint>
          <certificate>
            <chain>
              <name>TP-self-signed-1530096085</name>
              <certificate>
                <serial>01</serial>
                <certtype>self-signed</certtype>
              </certificate>
            </chain>
          </certificate>
        </pki>
      </crypto>
      <license>
        <udi>
          <pid>CSR1000V</pid>
          <sn>952DVZ4A2VB</sn>
        </udi>
        <boot>
          <level>
            <ax/>
          </level>
        </boot>
      </license>
      <line>
        <console>
          <first>0</first>
          <exec-timeout>
            <minutes>0</minutes>
            <seconds>0</seconds>
          </exec-timeout>
          <stopbits>1</stopbits>
        </console>
        <vty>
          <first>0</first>
          <last>4</last>
          <login>
            <local/>
          </login>
          <transport>
            <input>
              <input>ssh</input>
            </input>
          </transport>
        </vty>
      </line>
      <diagnostic xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-diagnostics">
        <bootup>
          <level>minimal</level>
        </bootup>
      </diagnostic>
    </native>
  </data>
</rpc-reply>
'''
