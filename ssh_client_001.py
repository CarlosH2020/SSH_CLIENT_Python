"""
Cliente SSH - version 1.2
By Carlos Henrique Barros Silva Campos
"""
import paramiko
print('=====================================')
print('#             SSH Client            #')
print('=====================================')
HOST = input('HOST:')
USER = input('USER:')
PASSWD = input('PASSWORD:')
try:
    client_ssh = paramiko.SSHClient()
    client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client_ssh.connect(hostname=HOST, username=USER, password=PASSWD)
except Exception as err:
    print(err)

while True:
    stdin, stdout, stderr = client_ssh.exec_command(input('(bash):'))
    for linha in stdout.readlines():
        if stderr:
            print(stderr)
        else:
            print(linha)
