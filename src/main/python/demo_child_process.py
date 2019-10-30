#!/usr/bin/env python3

import os
import subprocess
from sys import stderr

#status = os.system('python lotto.py')
#print(status)


#for line in os.popen('tasklist').readlines():
#    print(line)

#p = subprocess.run("python lotto.py", shell=True)
#print(p.returncode)


p = subprocess.run("tasklist", shell=True, capture_output=True)

if p.stdout:
    print(p.stdout)

if p.stderr:
    print(p.stdout)

