#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
# Les informations sont attendues en arguments
# exemple--> host=www.eni.fr textport= 80 fichier=index.html

import socket,sys

host = input("Entrez l'hôte (exple: www.google.fr): ")
textport = input("Entrez le numéro du port (exple: 80): ")
fichier = input("Entrez le fichier à lire (exple: index.html): ")

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error :
	print ("erreur lors de la création du socket : ")
	sys.exit(1)
try:
	port=int(textport)
except ValueError:
	try:
		port=socket.getservbyname(host,'tcp')
	except socket.error:
		print ("ne trouve pas le port ")
		sys.exit(1)
try:
	s.connect((host,port))
except socket.gaierror : #erreur d'adresse internet
	print ("erreur d'adresse de connexion au serveur :")
	sys.exit(1)
except socket.error: # vérifie si le socket a bien été créé ou erreur
	print ("erreur de connexion: ")
	sys.exit(1)
try:
    s.sendall(bytes("GET %s HTTP/1.0\r\n\r\n" % fichier + "\n", "utf-8"))
    #s.sendall("GET %s HTTP/1.0\r\n\r\n" % fichier)
except socket.error:
	print ("erreur d'envoi des données : %s " %e)
	sys.exit(1)
while 1:
	try:
		buf=s.recv(2048)
	except socket.error:
		print ("erreur de reception des données: %s" %e)
		sys.exit(1)
	if not len(buf):
		break
	print ("Le contenu de la page demandé: %s" % buf)



