from netmiko import ConnectHandler

config = {
    "device_type" : "cisco_ios",
    "host" : "158.192.152.223",
    "username" : "admin",
    "password" : "admin",
    "port" : 22
}

client = ConnectHandler(**config)

#vystup = client.send_command("sh ip int br")
#print(vystup)
for i in range (0, 1000):


    conf_prikazy = [
        "int lo"+str(i+555),
        "ip addr 11.222.33.49 255.255.255.255".format(i%254)
    ]

client.send_config_set(conf_prikazy)

client.send_command("sh ip int br")