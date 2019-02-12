import string
import random
l=string.printable
a=[]
string=['0x68','0x73','0x2e','0x00','0x7d','0x5c','0x46','0x06']
string.reverse()
print string
flag=''
c=0
f='a'
for i in string:
	b=int(i,0)
	while(1):
		check=''.join(f+random.choice(l) for _ in range(1))
		if((ord(check[0])^ord(check[1])==b)):
			print check[1]
			c=1
			break
	if(c==1):		
		f=check[1]


#}wz|`BzbDr}Dos*hDrhDb~iD}*ihoD|urhi~m~iD}wz|:f'''
#flag{Yay_if_th1s_is_yer_f1rst_gnisrever_flag!}
