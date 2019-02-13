string="t_nssiamwp_lsei_hatt{_gaalllF}"

new=[]
new1=[]
for i in range(1,len(string),2):
	new.append(string[i])
print new
for i in range(0,len(string),2):
	new1.append(string[i])
print new1[::-1]
print ''.join(new1[::-1])+''.join(new)

