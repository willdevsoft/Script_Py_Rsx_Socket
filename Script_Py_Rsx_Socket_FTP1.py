#!/usr/bin/env python
#--*-- coding:UTF-8 --*-- codage de caractéres informatiques 8 bits utilisé par site web
# voir RFC959 sur la norme du protocole FTP www.faqs.org/rfcs/rfc959.html
# nota: le site ftp.ibiblio.org fonctionne avec une connexion anonyme
# CR -> /r debut de ligne
# LF -> /n = saut de ligne
import socket
import time

host="ftp.ibiblio.org"
port=21
# 1-> Le serveur FTP envoie une banniére 
# 2-> identification via user et pwd
# fonction fini() pour afficher le resultat des requetes vers le serveur
def fini():
    data=s.recv(1024)
    print ("%s" % data)
    if data=="":
            pass

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(( host,port))
fini()
s.send(bytes("USER anonymous\r\n" + "\n", "utf-8"))
fini()
time.sleep( 5 )
s.send(bytes("PASS toto@tata.fr\r\n" + "\n", "utf-8"))
fini()
time.sleep( 5 )
s.send(bytes("HELP\r\n" + "\n", "utf-8"))
fini()
# il faut lancer QUIT\r\n pour clore la connexion
s.send(bytes("QUIT\r\n" + "\n", "utf-8"))
s.close()


