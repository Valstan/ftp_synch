import paramiko
from lopes import ftp_synch_host, ftp_synch_port, ftp_synch_username, ftp_synch_password

local_out_file = "Message_МИ_БР.xml"
remote_out_file = "/root/ftp_synch/Message_МИ_БР.xml"
local_in_file = "Message_БР_МИ.xml"
remote_in_file = "/root/ftp_synch/Message_БР_МИ.xml"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ftp_synch_host, ftp_synch_port, ftp_synch_username, ftp_synch_password)

ftp_client = ssh_client.open_sftp()
ftp_client.get(remote_in_file, local_in_file)
ftp_client.put(local_out_file, remote_out_file)
ftp_client.close()
