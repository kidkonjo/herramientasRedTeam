#!/bin/bash
import subprocess;
import optparse;

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface", help="Interface to change its IP address")
    parser.add_option("-I","--ip",dest="new_ip", help="New IP address")
    parser.add_option("-n","--netmask",dest="new_netmask", help="New netmask address")
    parser.add_option("-b","--broadcast",dest="new_broadcast", help="New broadcast address")
    parser.add_option("-m","--mac",dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        print("[!] Please specify an interface, use --help for more info.")
        
    return options

def change_ip(interface, new_ip):
    print("[+] Changing ip address for " + interface + " to " + new_ip)
    subprocess.call(["ifconfig", interface, new_ip])
    
def change_netmask(interface, new_netmask):
    print("[+] Changing netmask address for " + interface + " to " + new_netmask)
    subprocess.call(["ifconfig", interface, "netmask", new_netmask])
    
def change_broadcast(interface, new_broadcast):
    print("[+] Changing broadcast address for " + interface + " to " + new_broadcast)
    subprocess.call(["ifconfig", interface, "broadcast", new_broadcast])
    
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
if options.new_ip:
    change_ip(options.interface, options.new_ip)
if options.new_netmask:
    change_netmask(options.interface, options.new_netmask)
if options.new_broadcast:
    change_broadcast(options.interface, options.new_broadcast)
if options.new_mac:
    change_mac(options.interface, options.new_mac)