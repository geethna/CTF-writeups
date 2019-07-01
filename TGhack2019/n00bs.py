from pwn import *
import hashlib
p = remote('hash.tghack.no', 2001)
#hashes are : MD5 , SHA256 , SHA512
p.recvuntil('Good luck!\n')
for i in range(100):
    p.recvuntil('using ')
    hash = p.recvuntil(', ')
    hash = hash[:len(hash)-2]
    p.recvuntil('please: ')
    string = p.recvline().strip()
    print hash,string
    if(hash == "MD5"):
        value = hashlib.md5(string.encode())
        result = value.hexdigest()
    elif(hash == "SHA256"):
        value = hashlib.sha256(string.encode())
        result = value.hexdigest()
    elif(hash == "SHA512"):
        value = hashlib.sha512(string.encode())
        result = value.hexdigest()
    print result
    p.sendline(result)
p.interactive()
