import paramiko

host = "x.x.x.x"
port = 22
username = "root"
password = "password"

command_list = "ps -aef"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
print("Connection to Jenkins Server sucessful")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command_list)
exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error

for line in ssh_stdout:
    print(line.strip())

