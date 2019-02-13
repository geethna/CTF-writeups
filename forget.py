with open('wow', 'rb') as f:
	data = f.read()
a = ''
print data
for i in range(58):
	a += chr(ord(data[5*i+5+4104])^ord(data[i+5105]))
print a
