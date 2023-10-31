import paramiko

# create ssh client 
ssh_client = paramiko.SSHClient()

# remote server credentials
host = "sftp.ops.retailnext.net"
username = "7775ea64-6e85-11ee-87a5-c000f8cc7100"
password = "l3CC-CnlLCbAAsAaO3iK-kwx0dE"
port = 2022

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

ftp = ssh_client.open_sftp()
ftp.get("//custom_exports//phaseeight//PhaseEightHourlyData.txt", "//server_db1//scripts//Footfall//PhaseEightHourlyData.txt")

# close the connection
ftp.close()
ssh_client.close()