from pwn import *
from Crypto.Util.number import *
p = remote('bytes.tghack.no',2010)
for i in range(1000):
    a = p.recvline()
    print a
    if("number" in a):
        num = int(p.recvline().strip())
        print num
        num1 = long_to_bytes(num).encode("hex")
        p.sendline(num1)
        print num1
    elif("bytes" in a):
        num = p.recvline().strip()
        print num
        if(len(num)%2!=0):
            num = "0" + num
        print num + "---"
        num1 = bytes_to_long(num.decode("hex"))
        p.sendline(str(num1))
        print num1
    i=i+1
    print i
p.interactive()
