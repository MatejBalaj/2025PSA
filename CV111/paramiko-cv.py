from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy())

client.connect("158.193.152.248", username="admin", password="admin")

#stdin,stdout,stderr = client.exec_command("ip add print")
#print(stdout.read().decode("utf-8"))

#for riadok in stdout:
#    print(riadok, end="")
for i in range (0, 10):
    client.exec_command("interface bridge add name=lo"+str(i+1000))

stdin,stdout,stderr = client.exec_command("interface print")
print(stdout.read().decode("utf-8"))
