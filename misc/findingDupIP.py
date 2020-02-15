#sample Source List
ip_address = ["10.0.0.1", "10.0.0.1", "10.0.0.2", "12.0.3.1", "10.9.0.1", "12.0.1.1", "10.0.0.2"]   

ip_counts = {ip: ip_address.count(ip) for ip in set(ip_address)}

for ip, count in ip_counts.items():
    if count > 1:
        print(f"Dup IP:{ip} number of dup hosts {count}")
    else:
        continue

