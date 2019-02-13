s='J/TtC=&4&LJ'
import string
l=string.printable
b=['0','4','8']
'''for i in b:
   for j in l:
       if(ord(j)==(12^(ord(i)))):
           print i,j'''
for i in l:
    if(2*ord('&')==ord(i)):
        print i
