s='?5b9no=k!5<jW;h7W~b4#|'
s=s[::-1]
a=''
for i in range(22):
	a+=chr(ord(s[i])^12)
print a
n=''
new=''

for i in range(22):
	if(i%2==0):
		n=chr(ord(a[i])-4)
	else:
		n=chr(ord(a[i])+4)
	new+=n
print new
