import paramiko
from lopes import ftp_synch_host, ftp_synch_port, ftp_synch_username, ftp_synch_password

import os
import datetime

local_dir = datetime.datetime.now().strftime('%m-%d_%H')
os.makedirs(local_dir)

filenames = (
    "dbase.json",
    "mbase.json",
)
remote_dir = "/root/postopus/bases/"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ftp_synch_host, ftp_synch_port, ftp_synch_username, ftp_synch_password)
ftp_client = ssh_client.open_sftp()

for fname in filenames:
    ftp_client.get(remote_dir + fname, local_dir + '/' + fname)

ftp_client.close()
