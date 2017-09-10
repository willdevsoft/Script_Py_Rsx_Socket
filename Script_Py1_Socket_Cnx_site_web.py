#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#utilisation de la bibliothÃ©que socket pour accÃ©der aux diffÃ©rents services web
# tel que:  Web, FTP, mails
#normes communications TCP/UDP (voir RFC)
# Script Ã©tablissant une connexion Ã  l'hote sans Ã©changer de data
import socket

print ('creation du socket ...')

# CrÃ©ation de l'objet socket
# AF_INET --> utilisation de IPv4
# SOCK_STREAM --> utilisation de TCP ou SOCK_DGRAM --> utilisation de UDP
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print ('socket fait')
print ("connection a l'hote distant")

# connect --> connection Ã  l'hote distant + tuple (@IP + port)
s.connect(('www.eni.fr',80))

print ('connexion faite')

# send() --> communication avec le socket
r='GET /index.php HTML/1.1\r\n\r\n'
s.send(r.encode() )
data=s.recv(2048)
print (data)
s.close()

