'''s='xt=aok}x=~as}a~<<xw}'
flag=''
for i in s:
	flag+=chr((ord(i)-7)^5)
print flag	
#pD @ 0x004016b0 @a:arm:32
#export LD_LIBRARY_PATH="/path/to/sdk/lib"
#th3_mast3r_is_r00tus
'''
f=open('ma','r')
data=f.read()
my_list = data.splitlines()
import os
count=0
for i in my_list:
	print os.system('rasm2 -a mips -d '+i)
	count+=1
print count
