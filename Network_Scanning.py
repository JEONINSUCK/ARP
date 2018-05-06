from scapy.all import *


ans,unans = srp(scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.all.ARP(pdst="172.30.1.0/24"),timeout=2)
print(ans.summary())
"""ans, unans = scapy.layers.l2.arping(scapy.all.net, iface=scapy.all.interface, timeout=1, verbose=True)
for s, r in ans.res:
    line = r.sprintf("%Ether.src%  %ARP.psrc%")"""

res, unres = srp(scapy.all.Ether)