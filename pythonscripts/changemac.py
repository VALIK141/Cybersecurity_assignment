import subprocess

interface = "eth0" 
new_mac = "00:11:22:33:44:55"
subprocess.call(["ifconfig", eth0, "down"])
subprocess.call(["ifconfig", eth0, "hw", "ether", new_mac]) 
subprocess.call(["ifconfig", eth0, "up"])
