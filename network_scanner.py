import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=(ip))
    mac_request = scapy.Ether()
    mac_request.dst="ff:ff:ff:ff:ff:ff"
    arp_mac_request=mac_request/arp_request
    linked_list = scapy.srp(arp_mac_request, timeout=1,verbose=False)[0]
    print("----------------------------------------\nIP\t\tMAC ADDRESS\n----------------------------------------")
    for element in linked_list:
        print(element[1].psrc + "\t" + element[1].hwsrc)


ip = input("[+] Enter the Ip address and IP range: ")
print("[-] Scanning the result",ip)
scan(ip)
