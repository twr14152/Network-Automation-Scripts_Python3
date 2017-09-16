root@debian:/home/todd/gns3# ./netmiko_conf_mp_pools.py
Username: 
Password: 
Enter config commands seperated by ',': interface loopback 1, description this is a test
Enter the host IPs seperate with space: r1 r2 r3 r4 r5
Connected to host: r3
Connected to host: r2
Connected to host: r1
Connected to host: r5
Connected to host: r4
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#interface loopback 1
R3(config-if)# description this is a test
R3(config-if)#end
R3#

---- Elapsed time= 8.392916917800903
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#interface loopback 1
R2(config-if)# description this is a test
R2(config-if)#end
R2#

---- Elapsed time= 8.500743627548218
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#interface loopback 1
R1(config-if)# description this is a test
R1(config-if)#end
R1#

---- Elapsed time= 8.696260690689087
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R5(config)#interface loopback 1
R5(config-if)# description this is a test
R5(config-if)#end
R5#

---- Elapsed time= 8.971424341201782
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R4(config)#interface loopback 1
R4(config-if)# description this is a test
R4(config-if)#end
R4#

---- Elapsed time= 9.040150880813599
[None, None, None, None, None]
root@debian:/home/todd/gns3# 

  
**************
Adding an ACL
**************

todd@debian:~/gns3$ ./netmiko_conf_mp_pools.py 
Username: 
Password: 
Enter config commands seperated by ',': ip access-list extended test_acl, permit tcp any any log, permit udp any any log
Enter the host IPs seperate with space: r1 r2 r3 r4 r5
Connected to host: r2
Connected to host: r4
Connected to host: r5
Connected to host: r3
Connected to host: r1
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R5(config)#ip access-list extended test_acl
R5(config-ext-nacl)# permit tcp any any log
R5(config-ext-nacl)# permit udp any any log
R5(config-ext-nacl)#end
R5#

---- Elapsed time= 9.461827039718628
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#ip access-list extended test_acl
R3(config-ext-nacl)# permit tcp any any log
R3(config-ext-nacl)# permit udp any any log
R3(config-ext-nacl)#end
R3#

---- Elapsed time= 9.696628332138062
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#ip access-list extended test_acl
R1(config-ext-nacl)# permit tcp any any log
R1(config-ext-nacl)# permit udp any any log
R1(config-ext-nacl)#end
R1#

---- Elapsed time= 9.735490322113037
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R4(config)#ip access-list extended test_acl
R4(config-ext-nacl)# permit tcp any any log
R4(config-ext-nacl)# permit udp any any log
R4(config-ext-nacl)#end
R4#

---- Elapsed time= 9.76802921295166
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#ip access-list extended test_acl
R2(config-ext-nacl)# permit tcp any any log
R2(config-ext-nacl)# permit udp any any log
R2(config-ext-nacl)#end
R2#

---- Elapsed time= 9.791200399398804
[None, None, None, None, None]
todd@debian:~/gns3$ 
