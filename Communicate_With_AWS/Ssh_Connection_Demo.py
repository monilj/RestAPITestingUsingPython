import paramiko as parmiko_demo
from util.configurations import *

# Start connection
userName = getConfig()['Linux_Server']['username']
password = getConfig()['Linux_Server']['password']
host = getConfig()['Linux_Server']['host']
port = getConfig()['Linux_Server']['port']
sshCo = parmiko_demo.SSHClient()
sshCo.set_missing_host_key_policy(parmiko_demo.AutoAddPolicy())
sshCo.connect(host, port, userName, port)
