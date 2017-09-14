#!/usr/bin/env python
# création d'un serveur en 4 étapes:
# 1-> création d'une socket
# 2-> rajouter option au socket
# 3-> lier à un port (bind)
# 4-> Ecoute des connexions (listen)

import socket,time

#host = input("Entrez l'adresse IP de la carte réseau du serveur: ")
port = input("Entrez le port du serveur: ")
host =socket.gethostbyname(socket.gethostname()) #récupére le hostname du serveur
print ("Le host= %s et le port=" % host %port)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((host,port)) #lier (bind) l'adresse avec le port

s.listen(5) # (5)=nombre de connexions acceptable dans la queue de réception 
#while 1:
#	time.sleep(1)
#	print ("en attente (ctrl+c pour exit)")
 
client,adresse=s.accept() #accepte un client et création du socket client pour discuter avec le client
print ("client connecté:%s" %adresse) #récupération de l'adresse et du port
clientname=client.getpeername()
client.close() # fermeture du socket client
s.close() #fermeture du socket serveur