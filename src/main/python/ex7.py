#!/usr/bin/env python3

'''

'''

import re

def main():
    
    unused_port_numbers = set()
    
    with open(r'C:\Windows\System32\drivers\etc\services') as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            
            line = line.strip()
            if not line:
                continue
            
            # Remove comments
            line = re.sub(r'#.*$', "", line)


            m = re.search(r'(\d+)/(udp|tcp)\s*(.*)', line)
            if m:
                port_number = int(m.group(1))
                alias = m.group(3).strip()
                if port_number <= 200 and alias:
                    unused_port_numbers.add(port_number)
                

    for port_number in sorted(unused_port_numbers):
        print(port_number)

if __name__ == "__main__":
    main()

