#!/usr/bin/env python
# création d'un serveur en 4 étapes:
# 1-> création d'une socket
# 2-> rajouter option au socket
# 3-> lier à un port (bind)
# 4-> Ecoute des connexions (listen)

import socket,time

host = input("Entrez l'adresse IP de la carte réseau: ")
#host = "195.168.1.14" ;
socket.gethostbyname(socket.gethostname())
print ("Le host est : %s" % host)
port=1234

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port)) #lier (bind) l'adresse avec le port

s.listen(5) # (5)=nombre de connexions acceptable dans la queue de réception 
while 1:
	time.sleep(1)
	print ("en attente (ctrl+c pour exit)")
    