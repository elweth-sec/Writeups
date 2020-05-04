from Crypto.Util.number import inverse
import binascii 
import codecs


p = 650655447295098801102272374367
q = 972033825117160941379425504503
c = 63775417045544543594281416329767355155835033510382720735973
e = 65537
n = p*q

phi = (p-1) *(q-1)
d = inverse(e,phi)

uncipher = pow(c,d,n)
print("## Données ## ")
print("[+] n: " + str(n))
print("[+] e: " + str(e))
print("[+] cipher: " + str(c))
print("\n## Calculs ##")
print("[+] p: " + str(p))
print("[+] q: " + str(q))
print("\n## Résultat ##")
print("[+] uncipher: " + str(uncipher) + "\n")
print("[+] Flag : FCSC{"+str(uncipher)+"}\n")