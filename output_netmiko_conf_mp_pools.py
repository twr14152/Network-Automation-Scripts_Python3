root@debian:/home/todd/gns3# python3 netmiko_conf_mp_pools.py 
Username: 
Password: 
Enter config commands seperated by ',': interface loopback 0, description this_is_a_test
Enter the host IPs seperate with space: r1 r2 r3 r4 r5
Connected to host: r2
Connected to host: r4
Connected to host: r3
Connected to host: r1
Connected to host: r5
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#interface loopback 0
R2(config-if)# description this_is_a_test
R2(config-if)#end
R2#

---- End get config sequential, elapsed time= 8.60096549987793
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#interface loopback 0
R1(config-if)# description this_is_a_test
R1(config-if)#end
R1#

---- End get config sequential, elapsed time= 8.646637916564941
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R4(config)#interface loopback 0
R4(config-if)# description this_is_a_test
R4(config-if)#end
R4#

---- End get config sequential, elapsed time= 8.889029264450073
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#interface loopback 0
R3(config-if)# description this_is_a_test
R3(config-if)#end
R3#

---- End get config sequential, elapsed time= 8.97205901145935
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R5(config)#interface loopback 0
R5(config-if)# description this_is_a_test
R5(config-if)#end
R5#

---- End get config sequential, elapsed time= 9.072935819625854
[None, None, None, None, None]
root@debian:/home/todd/gns3# 
