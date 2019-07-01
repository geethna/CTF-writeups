from pwn import *
p = remote('34.68.81.63', 6666)
both = "Both are equally heavy"
left_light = "The left is lighter than the right"
left_heavy = "The left is heavier than the right"
p.recvuntil("Example weigh balls at position 1,2,3 vs 4,5,6: 1,2,3 4,5,6")
for i in range(50):
    print p.recvline()
    print p.recvuntil(": ")
    p.sendline("1,2,3,4 5,6,7,8")
    a = p.recvline().strip()
    print a
    if (a == both):
        print p.recvuntil("Weighting 2: ")
        p.sendline("8,9 10,11")
        a = p.recvline().strip()
        print a
        if(a == both):
            print p.recvuntil("Weighting 3: ")
            p.sendline("11 12")
            a = p.recvline().strip()
            if(a == left_heavy):
                p.recvuntil("The fake ball is :")
                p.sendline("12")
            elif(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("12")
            elif(a == left_light):
                p.recvuntil("The fake ball is :")
                p.sendline("12")
        elif(a == left_light):
            print p.recvuntil("Weighting 3: ")
            p.sendline("10 11")
            a = p.recvline().strip()
            print a
            if(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("9")
            elif(a == left_light):
                p.recvuntil("The fake ball is :")
                p.sendline("11")
            elif(a == left_heavy):
                p.recvuntil("The fake ball is :")
                p.sendline("10")
        elif(a == left_heavy):
            p.recvuntil("Weighting 3: ")
            p.sendline("10 11")
            a = p.recvline().strip()
            print a
            if(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("9")
            elif(a == left_heavy):
                p.recvuntil("The fake ball is :")
                p.sendline("11")
            elif(a == left_light):
                p.recvuntil("The fake ball is :")
                p.sendline("10")
    elif (a == left_heavy):
        print p.recvuntil("Weighting 2: ")
        p.sendline("1,2,5 3,6,9")
        a = p.recvline().strip()
        print a
        if(a == both):
            print p.recvuntil("Weighting 3: ")
            p.sendline("7 8")
            a = p.recvline().strip()
            print a
            if(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("4")
            elif(a == left_light):
                p.recvuntil("The fake ball is :")
                p.sendline("7")
            else:
                p.recvuntil("The fake ball is :")
                p.sendline("8")
        elif(a == left_heavy):
            print p.recvuntil("Weighting 3: ")
            p.sendline("1 2")
            a = p.recvline().strip()
            print a
            if(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("6")
            elif(a == left_heavy):
                p.recvuntil("The fake ball is :")
                p.sendline("1")
            elif(a == left_light):
                p.recvuntil("The fake ball is :")
                p.sendline("2")
        elif(a == left_light):
            print p.recvuntil("Weighting 3: ")
            p.sendline("5 9")
            a = p.recvline().strip()
            print a
            if(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("3")
            elif(a == left_light):
                p.recvuntil("The fake ball is :")
                p.sendline("5")
            elif(a == left_heavy):
                p.recvuntil("The fake ball is :")
                p.sendline("9")
    elif(a == left_light):
        print p.recvuntil("Weighting 2: ")
        p.sendline("5,6,1 7,2,9")
        a = p.recvline().strip()
        print a
        if(a == both):
            print p.recvuntil("Weighting 3: ")
            p.sendline("3 4")
            a = p.recvline().strip()
            print a
            if(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("8")
            elif(a == left_light ):
                p.recvuntil("The fake ball is :")
                p.sendline("3")
            elif(a == left_heavy):
                p.recvuntil("The fake ball is :")
                p.sendline("4")
        elif(a == left_heavy):
            print p.recvuntil("Weighting 3: ")
            p.sendline("5 6")
            a = p.recvline().strip()
            print a
            if(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("2")
            elif(a == left_heavy):
                p.recvuntil("The fake ball is :")
                p.sendline("5")
            elif(a == left_light):
                p.recvuntil("The fake ball is :")
                p.sendline("6")
        elif(a == left_light ):
            print p.recvuntil("Weighting 3: ")
            p.sendline("1 9")
            a = p.recvline().strip()
            print a
            if(a == both):
                p.recvuntil("The fake ball is :")
                p.sendline("7")
            elif(a == left_light):
                p.recvuntil("The fake ball is :")
                p.sendline("1")
            elif(a == left_heavy):
                p.recvuntil("The fake ball is :")
                p.sendline("1")
p.interactive()
