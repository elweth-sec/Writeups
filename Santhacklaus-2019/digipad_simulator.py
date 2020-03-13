#!/usr/bin/python

import socket

def connect():
	host = "46.30.204.44"
	port = 4000

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	#Premiere reponse
	reponse = s.recv(1024)
	print reponse

	#Deuxieme reponse
	reponse2 = s.recv(1024)
	print reponse2

	# on analyse la reponse pour voir quels chiffres manquent
	code = ""
	for i in range(0,10):
		if str(i) not in reponse:
			code = code + str(i)
			print "[>] " +str(i) + " n'est pas present. On l'ajoute"

	print "Envoie de " + str(code)
	s.send(code)

	# on recoit la reponse : code bon ou code faux
	reponse3 = s.recv(1024)
	print reponse3

	if "Wrong code, bye" in reponse3:
		return "incorrect"
	else:
		return "correct"

	print "Close"
	s.close()


cpt = 0
while connect() != "correct":
	connect()
	cpt = cpt + 1

print "Trouve en " + str(cpt) + " essais"
