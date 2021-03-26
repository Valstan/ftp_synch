import os
import paramiko

'''ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('ovz1.id45d.n0ykp.vps.myjino.ru:49312', username="root", password="password")
sftp = ssh.open_sftp()
localpath = 'Message_БР_МИ.xml' # Message_МИ_БР.xml
remotepath = '/root/ftp_synch/Message_БР_МИ.xml'
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()'''


host = "ovz1.id45d.n0ykp.vps.myjino.ru"
port = 49312
password = "root"
username = "nitro2000"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

sftp = ssh.open_sftp()

path = "/root/ftp_synch/Message_БР_МИ.xml"
localpath = "Message_БР_МИ.xml"
sftp.put(localpath, path)

sftp.close()
ssh.close()