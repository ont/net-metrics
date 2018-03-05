#!/usr/bin/python3

import re
import sys
import json
import subprocess
from collections import Counter

def ips():
    r = re.compile(r":" + sys.argv[1] + r"\b" )
    p = subprocess.Popen("netstat -ant", shell=True, stdout=subprocess.PIPE)
    for line in p.stdout.readlines():
        line = line.decode('utf-8')
        if r.search(line) and "ESTABLISHED" in line:
            client_ip_port = line.split()[4]
            ip = client_ip_port.split(':')[0]
            yield ip

c = Counter(ips())
data = [{"hosts" : hosts, "pconns": pconns} for pconns, hosts in Counter(c.values()).items()]
print(json.dumps(data))

