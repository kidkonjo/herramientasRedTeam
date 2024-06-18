#!/bin/bash
import subprocess;
import optparse;

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface", help="Interface to change its IP address")
    parser.add_option("-i","--ip",dest="new_ip", help="New IP address")
    return parser.parse_args()

def change_ip(interface, new_ip):
    print("[+] Changing ip address for " + interface + " to " + new_ip)
    subprocess.call(["ifconfig", interface, new_ip])

(options, arguments) = get_arguments()
change_ip(options.interface, options.new_ip)
