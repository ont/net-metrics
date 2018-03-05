#!/usr/bin/python3

import re
import sys
import json
import subprocess
from collections import Counter

def ips():
    r_dport = re.compile(r"dport=" + sys.argv[1] + r"\b" )
    r_src = re.compile(r"src=(\S+)")

    p = subprocess.Popen("conntrack -L", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    for line in p.stdout.readlines():
        line = line.decode('utf-8')
        if r_dport.search(line) and "ESTABLISHED" in line:
            m = r_src.search(line)
            if m:
                yield m.group(1)

c = Counter(ips())
data = [{"hosts" : hosts, "pconns": pconns} for pconns, hosts in Counter(c.values()).items()]
print(json.dumps(data))
