import string
import random
from hashlib import md5
l='!@_{}'
hashes=['9f9bd93c746d42c056754dd9607a7ff9','5b99e41b25e90adc18f7dcdf8dcb7298','95ae5f38b5e4ab0d9d11df14f11046cf','f0f7af88ab3aea458526510b1877ab62','676d5fb511b9b670b7c9b12c69771f6d',
'6b78f09b932f0519cc29508017bf361d','ece3a0446786d5f863ca976fd3c8e2ac','e19eca4206a23070180a3a2ec947b3b7','b507848b93b4644d0dbf1fc83e8b349c','2cac4d5aa5fc42f9d7dfc112bd7fac32',
'55049938be97380188ee360b22a29756','cefa5bd3165bb00274063e75bc28014f','040a35411852126d8e76c106d867cf8b','f99cc38ac9fcae359a14fb5777c42400','c4351fcc350e725e7f89b4c2524dd0a9',
'e4f6c86600cae1f5c138ce50d66578dc','010a2cbcd80f9f15d421b000f40495b3','3e4c9ecd6a2dbbe65369c57a04481431','2adc099e0c6bb1d43a08a6c41b2c7220','5990a3dafba11c058dc6d22facf2a7ab']
c=0
flag=''
while(1):
	check=''.join(random.choice(string.letters+ string.digits+l) for _ in range(4))
	if(md5(md5(check).hexdigest()).hexdigest()==hashes[c]):
		flag+=check
		print flag
		c+=1
	if(c==20):
		break
