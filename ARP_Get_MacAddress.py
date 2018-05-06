from scapy.all import *
import socket


results, unanswered = sr(scapy.all.ARP(op=scapy.all.ARP.who_has, psrc=socket.gethostbyname(socket.gethostname())
, pdst='172.30.1.196'),timeout=1)

req = results[0][0]
res = results[0][1]

Target_Mac = res.fields['hwsrc']
Target_IP = res.fields['psrc']
My_Ip = res.fields['pdst']
My_Mac = res.fields['hwdst']

print(Target_IP)
print(Target_Mac)
print(My_Ip)
print(My_Mac)

"""Timeout = 2
answered, unanswered = srp(scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.all.ARP(pdst="172.30.1.196"), timeout=Timeout, verbose=False)
print(answered.filter(func=))
 print(unanswered.summary())"""