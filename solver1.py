from z3 import *
n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18=BitVecs('n5 n6 n7 n8 n9 n10 n11 n12 n13 n14 n15 n16 n17 n18',32)
s=Solver()
s.add(n6>32,n7>32,n8>32,n9>32,n10>32,n11>32,n12>32,n13>32,n14>32,n15>32,n16>32,n17>32,n18>32)
s.add(n6<128,n7<128,n8<128,n9<128,n10<128,n11<128,n12<128,n13<128,n14<128,n15<128,n16<128,n17<128,n18<128)
s.add(n5==ord('{'))
s.add(n18==ord('}'))
s.add(n5+(n7^n6)%4==113) #fun4
s.add((n12*n9)^(2*n10)==8983) #fun5
s.add((311-n13)^(n14*n11)==9819)#fun6
s.add((((n15*n17)+n16)*202)-(n16*n17)==1998612)#fun7
s.add((((n18*n17)*(n18+n17))^4919)-(n17-(n17^n18)+n17)==2816180)#final

while s.check() == sat:
        r = s.model()
	
        ss5 = r[n5]
        ss6 = r[n6]
        ss7 = r[n7]
        ss8 = r[n8]
        ss9 = r[n9]
        ss10 = r[n10]
        ss11 = r[n11]
        ss12 = r[n12]
        ss13 = r[n13]
        ss14 = r[n14]
        ss15 = r[n15]
        ss16 = r[n16]
        ss17 = r[n17]
	ss18 = r[n18]
        string1 = ''
	string1 += chr(ss5)
        string1 += chr(ss6)
        string1 += chr(ss7)
        string1 += chr(ss8)
        string1 += chr(ss9)
        string1 += chr(ss10)
        string1 += chr(ss11)
        string1 += chr(ss12)
        string1 += chr(ss13)
        string1 += chr(ss14)
        string1 += chr(ss15)
        string1 += chr(ss16)
        string1 += chr(ss17)
	string1 += chr(ss18)

	print string1


s.add( Or(n5 != ss5, n6 != ss6, n7 != ss7, n8 != ss8, n9 != ss9, n10 != ss10, n11 != ss11, n12 != ss12, n13 != ss13, n14 != ss14, n15 != ss15, n16 != ss16, n17 != ss17, n18 !=ss18))



