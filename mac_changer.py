import subprocess
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface", help="interface to change mac address")
    parser.add_option("-m","--mac_address", dest="mac_address", help="it will change to new mac address ")
    (options, arguments) = parser.parse_args()
    if not options.interface:
         parser.error("you have not entered interface go through the --help to know about interface ")
    elif not options.mac_address:
         parser.error("you have not entered mac_address go though the --help to know about mac_address ")
    return options

def mac_changer(interface, mac_address):
    print("[+] Changed new Mac_address " + interface + " to " + mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])



options = get_arguments()
mac_changer(options.interface, options.mac_address)
















