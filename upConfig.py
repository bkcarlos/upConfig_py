#!/usr/bin/env python
#coding=UTF-8

import paramiko

import os
import socket
import select


def sshScpPut(ip, port, user, passwd, localDir, remoteDir):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ip, port=port, username=user, password=passwd)

    if not remoteDir[-1] == '/':
        remoteDir = remoteDir + '/'

    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()

    files = os.listdir(localDir)
    for file in files:
        if os.path.splitext(file)[-1] == '.txt':
            localfilePath = localDir + "\\" + file
            if os.path.isfile(localfilePath):
                remoteFilePath = remoteDir + "/" + file
                cmdStr = r"rm -rvf " + remoteFilePath
                stdin, stdout, stderr = ssh.exec_command(cmdStr)
                print(stdout.readlines())

                sftp.put(localfilePath, remoteFilePath)
                cmdStr = r"ls " + remoteFilePath
                stdin, stdout, stderr = ssh.exec_command(cmdStr)
                strResReads = stdout.readlines()
                for strRes in strResReads:
                    if(strRes.find(file) != -1):
                        print("up", file, "success")
                        break;

    sftp.close()
    ssh.close()

if __name__ == "__main__":
    ip = "10.0.0.128"
    port = 22
    user = "root"
    passwd = "passwd"

    localDir = r".\Config"
    remoteDir = r"/tmp/"

    sshScpPut(ip, port, user, passwd, localDir, remoteDir)
    print("UpConfig success")



