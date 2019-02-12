from z3 import *
x=Real('x')
s=Solver()
s.add(x*(x-14)==-49)
s.check()
m=s.model()
key=type(1)(m[x])
some="akf`|3tXb32~X3tX6sX`4stz"
flag=''
for i in some:
    flag+=chr(ord(i)^key)
print flag

