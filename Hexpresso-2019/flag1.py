#!/usr/bin/python
#!*--*-- encoding:utf-8--*--

game = [116, 228, 203, 270, 334, 382, 354, 417, 
         485, 548, 586, 673, 658, 761, 801, 797, 
         788, 850, 879, 894, 959, 1059, 1071, 1140, 
         1207, 1226, 1258, 1305, 1376, 1385, 1431, 1515]

u_u = "CTF.By.HexpressoCTF.By.Hexpresso"

u_u_texte = []
u_u_charcode = []

print "[*] Conversion en charcode de : \t" + u_u

for val in u_u:
     u_u_texte.append(val)
     u_u_charcode.append(ord(val))

print u_u_texte
print u_u_charcode
flag = ""

i=0
for val in game:
     decode =  val - (u_u_charcode[i] + i*42 )
     flag = flag + str(chr(decode))
     i=i+1

print "\n[FLAG] : \t " + flag
print "\n[+] Prochaine étape : \t ctf.hexpresso.fr/"+flag 
