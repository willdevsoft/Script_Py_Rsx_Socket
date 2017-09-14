#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
# Script permettant d'établir une discussion client-serveur
# test avec netcat (necessite le rajout de /n aprés le mot fin
#Pensez à le supprimer si utilisation du prog client

import socket

host=''
port = 1338

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
client,adresse=s.accept() #socket client pour discuter avec lui
print ("adresse du client: %s" %adresse)
print ("nom du client: " + client.getpeername())
client.send("Bonjour toi\n entrez votre mot ou fin si vous voulez arreter la discussion\n")
# A partir de la boucle while la discussion commence entre le serveur et le client
# La discussion s'arretera avec le mot fin
while 1:
	data=client.recv(1024)
	if data=="fin\n":
		break
	print ("Client > " +  data)
	mot=raw_input("Serveur > ")
	client.send(mot)
client.close()
s.close()
