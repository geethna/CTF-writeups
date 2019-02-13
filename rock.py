a="FLAG23456912365453475897834567"
b=''
for i in a:
	b+=chr((ord(i)-9)^16)
print b
c=''
for j in b:
        c+=chr((ord(j)-20)^80)
print c

