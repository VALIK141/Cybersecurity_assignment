import subprocess

interface = "eth0"
subprocess.call(["sudo", "ifconfig", "eth0", "down"])
subprocess.call(["sudo", "iwconfig", "eth0", "mode", "monitor"])
subprocess.call(["sudo", "ifconfig", "eth0", "up"])
