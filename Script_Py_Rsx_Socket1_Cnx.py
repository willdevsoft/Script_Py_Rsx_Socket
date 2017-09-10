#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#utilisation de la bibliothéque socket pour accéder aux différents services web
# tel que:  Web, FTP, mails
#normes communications TCP/UDP (voir RFC)
# Script établissant une connexion Ã  l'hote sans échanger de data
import socket

print ('creation du socket ...')

# Création de l'objet socket
# AF_INET --> utilisation de IPv4
# SOCK_STREAM --> utilisation de TCP ou SOCK_DGRAM --> utilisation de UDP
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print ('socket fait')
print ("connection a l'hote distant")

# connect --> connection Ã  l'hote distant + tuple (@IP + port)
s.connect(('www.eni.fr',80))

print ('connexion faite')

# send() and recv()--> communication avec le socket en TCP
# sendto() and recvfrom()--> communication avec le socket en UDP
# récupération d'une partie 2048 octets)de la page web
r='GET /index.php HTML/1.1\r\n\r\n'
s.send(r.encode() )
data=s.recv(2048)
print (data)
s.close()

