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

# Executing Commands
# stdin, stdout, stderr = sshCo.exec_command("ls -a")
stdin, stdout, stderr = sshCo.exec_command("cat <file_name>")
lines = stdout.readlines()
print(lines[1])

# Upload file
sftpF = sshCo.open_sftp()
destinationPath = '<filePath/fileName>'
localPath = '<filePath_from_where_you_uploads>'
sftpF.put(localPath, destinationPath)

# Trigger Batch commands
sshCo.exec_command("python <fileName.py>")

# Download the file in to local system
sftpF.get('<filePath_from_where_to_download>', 'destination_folder_in_local_Machine')

# Parse output file and write assertion on data
sshCo.close()
