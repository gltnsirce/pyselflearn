#!/usr/bin/python3

import subprocess
import os
import sys

beginIP = input('Enter the starting IP address:')
endIP = input('Enter the ending IP address:')

with open(os.devnull, "wb") as limbo:
    for ping in range(int(beginIP),int(endIP)):
        addr = "10.62.91." + str(ping)
        res = subprocess.Popen(['ping', '-c', '1', "-n" , "-w" , "2" ,addr],
                stdout = limbo,
                stderr = limbo).wait()
        if res:
            print( addr, '\x1b[1;31m'+'inactive'+'\x1b[0m')         # Red code
        else:
            print( addr, '\x1b[1;32m'+'active'+ '\x1b[0m')          # Green code
