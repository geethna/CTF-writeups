from pwn import *
p = remote('math.tghack.no', 10000)
for i in range(1000):
    p.recvline()
    eq = p.recvline().split(' ')
    if(eq[1] == '+'):
        res = int(eq[0]) + int(eq[2].strip())
    elif(eq[1] == '-'):
        res = int(eq[0]) - int(eq[2].strip())
    elif(eq[1] == '*'):
        res = int(eq[0]) * int(eq[2].strip())
    elif(eq[1] == '%'):
        res = int(eq[0]) % int(eq[2].strip())
    elif(eq[1] == '/'):
        res = int(eq[0]) / int(eq[2].strip())
    print i
    print eq
    print res
    p.sendline(str(res))
    p.recvline()
p.interactive()
