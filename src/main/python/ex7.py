#!/usr/bin/env python3

'''

'''

import re

def main():
    with open(r'C:\Windows\System32\drivers\etc\services') as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            
            line = line.strip()
            if not line:
                continue
            
            # Remove comments
            line = re.sub(r'#.*$', "", line)
            print(line)
            
            parts = re.split(r'\s+', line)
            
    

if __name__ == "__main__":
    main()

