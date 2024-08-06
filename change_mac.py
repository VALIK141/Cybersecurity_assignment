!#/usr/bin/python


import os
import subprocess

subprocess.call("sudo ifconfig eth0 down", shell = True)
subprocess.call("sudo ifconfig eth0 hw ether 00:88:99:77:66:55", shell = True)
subprocess.call("sudo ifconfig eth0 hw up", shell = True)

