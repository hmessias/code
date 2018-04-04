#! /usr/bin/env python3

import pprint
import subprocess
import re
ips = []

def get_routers(IP_WWW): #this function issues the traceroute command against some destinations to get the routers throughout the path.
    completed = subprocess.run(
        ['traceroute', '-n', IP_WWW], #calls the command line traceroute
        stdout=subprocess.PIPE, #saves the standard output messages
        stderr=subprocess.PIPE, #saves the error messages
        universal_newlines=True
    )

    hops = completed.stdout.splitlines() #gets the standard output and extract just the ip address of the hops
    hops = hops[1:-1]
    for hop in hops:
        findexp = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', hop) #regex expression to get a set of 4 numbers within up to 3 digits separeted for dots from the standard output
        ips.extend(findexp)
    return



def main(): #this function will provide the destinatios ips to get a list of router's ips
    sites = ['8.8.8.8', 'osnews.com', 'yahoo.com', 'facebook.com', 'google.com'] #list of destinations
    for site in sites:
        get_routers(site)

    
    unique_ips = [] #this part will create a list of unique ips from the global information
    for ip in ips:
        if ip not in unique_ips:
            unique_ips.append(ip)
    
    pprint.pprint(unique_ips) # print list of unique ips
    return

if __name__ == "__main__":
    main()