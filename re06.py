import base64
string='iB6WcuCG3nq+fZkoGgneegMtA5SRRL9yH0vUeN56FgbikZFE1HhTM9R4tZPghhYGFgbUeHB4tEKRRNR4Ymu0OwljQwmRRNR4jWBweOKRRyCRRAljLGQ='
dec=base64.b64decode(string).decode('UTF-16LE')
new=''
import string
l='!@_{}'
chars=string.letters+ string.digits+l
def encode(s,e,n):
	array=[]
	while(e!=0):
		array.append(e%2)
		e/=2
	num2=1
	for i in range(len(array)-1,-1,-1):
		num2=num2*num2%n
		if(array[i]==1):
			num2=num2*ord(s)%n
	return num2
flag=''
for i in dec:
	for j in chars:
		var=encode(j,9157,41117)
		if(var==ord(i)):
			flag+=j
print flag
