from scapy.all import sniff, ARP

def arp_callback(packet):
    if ARP in packet and packet[ARP].op in (1, 2):
        return packet.sprintf("%ARP.hwsrc% | %ARP.psrc%")

print sniff(prn=arp_callback, filter="arp", store=0)
