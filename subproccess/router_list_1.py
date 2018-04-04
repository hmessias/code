#! /usr/bin/env python3

import pprint
import subprocess
import re
ips = []

def get_routers(IP_WWW):
    completed = subprocess.run(
        ['traceroute', '-n', IP_WWW],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    hops = completed.stdout.splitlines()
    hops = hops[1:-1]
    for hop in hops:
        findexp = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', hop)
        ips.extend(findexp)
    return

def main():
    sites = ['8.8.8.8', 'osnews.com', 'yahoo.com', 'facebook.com', 'google.com']
    for site in sites:
        get_routers(site)

    ips_Unique = list(set(ips)) # remove duplicates by creating a set
    pprint.pprint(ips_Unique) # print list of unique ips
    return

if __name__ == "__main__":
    main()