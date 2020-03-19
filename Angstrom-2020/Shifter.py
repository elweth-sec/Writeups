import socket
import sys

tab_fibonacci =[0 ,1 ,1 ,2 ,3 ,5 ,8 ,13 ,21 ,34 ,55 ,89 ,144 ,233 ,377 ,610 ,987 ,1597 ,2584 ,4181 ,6765 ,10946 ,17711 ,28657 ,46368 ,75025 ,121393 ,196418 ,317811 ,514229 ,832040,1346269 ,2178309 ,3524578 ,5702887 ,9227465 ,14930352 ,24157817 ,39088169 ,63245986 ,102334155 ,165580141 ,267914296 ,433494437 ,701408733 ,1134903170,1836311903,2971215073,4807526976,7778742049 ]

def decrypt(key, message):
	message = message.upper()
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = ""
	for letter in message:
		if letter in alpha:
			letter_index = (alpha.find(letter) - key) % len(alpha)
			result = result + alpha[letter_index]
		else:
			result = result + letter
	return result

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("misc.2020.chall.actf.co", 20300))

# Traitement pour recuperer la cle
rep = s.recv(1024).decode("latin-1")
rep = rep.split(" ")
key = rep[-2]
key=key.split("=")[1]
final_key = key.replace(":","").replace("\n","")
final_key = int(final_key)

# Traitement pour recuperer le texte
message_chiffre =  rep[50]
message_dechiffre = decrypt(-int(tab_fibonacci[final_key]), message_chiffre)
print("Message = " + message_chiffre + " | Key = " + str(final_key) + " | Decrypt = " + message_dechiffre)

message_dechiffre = message_dechiffre + "\n"
s.send(message_dechiffre.encode("latin-1"))

while True:
	rep = s.recv(1024).decode("latin-1")
	rep = rep.split(" ")
	if "Shift" not in rep:
		print("FLAG = " + rep[0])
		sys.exit(1)
	key = rep[3]
	key=key.split("=")[1]
	final_key = key.replace(":","").replace("\n","")
	final_key = int(final_key)
	message_chiffre =  rep[1]
	message_dechiffre = decrypt(-int(tab_fibonacci[final_key]), message_chiffre)

	print("Message = " + message_chiffre + " | Key = " + str(final_key) + " | Decrypt = " + message_dechiffre)
	message_dechiffre = message_dechiffre + "\n"
	s.send(message_dechiffre.encode("latin-1"))

