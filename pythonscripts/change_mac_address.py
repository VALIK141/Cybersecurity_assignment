import os
import subprocess

subprocess.call("sudo ifconfig etho down", shell=True)
subprocess.call("sudo ifconfig eth0 hw ether 33:22:44:00:77:44", shell=True)
subprocess.call("sudo ifconfig eth0 up", shell=True)
