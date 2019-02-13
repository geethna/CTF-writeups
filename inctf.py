s="h4v3n0M0utH&1mStsCr34m"
c=""
n=12
h=""
for i in range(0,22):
	c+=chr(ord(s[i])^n)
b="FLAG{7h1S_fl49_1S_7074lLy_f4K3_S0rrY}"
f="n07_4_k3Y_R34LLy_b7W_l1K3_7074LlY"
for i in range(0,len(f)):
	h+=chr(ord(b[i])^ord(f[i]))
bn=""
for i in range(0,22):
	bn+=chr(ord(h[i])^ord(c[i]))
print bn
