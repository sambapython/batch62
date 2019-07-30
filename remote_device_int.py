import paramiko as pmk
ssh = pmk.SSHClient()
ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
ssh.connect("localhost",username="khyaathidajngo",password="django")
#inp,outp,errp = ssh.exec_command("mkdir local")
#cmd="ls -l"
'''
cmd="echo django|sudo -S ls /proc"
inp,outp,errp = ssh.exec_command(cmd)
print("err:",errp.read())
print("out:",outp.read())
'''
sftp = ssh.open_sftp()
#sftp.put("/home/khyaathidajngo/local/content.odt",
#	"/home/khyaathidajngo/remote/content.odt")
sftp.get("/home/khyaathidajngo/remote/content.odt",
	"/home/khyaathidajngo/local/content2.odt")
