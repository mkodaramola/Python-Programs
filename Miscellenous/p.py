


c = "8/4-2+4-9x12+7/10x6/3-17-4x5"

def subMub(t):
	c1 = 0
	c2 = 0
	nnt =""
	nt = ""
	for i in t:
		if i == '/':
			nt = t[c1+1:]
			for j in nt:
				if j=='/' or j =='+' or j =='-' or j =='x':
					nnt = nt[:c2]
					break
				c2+=1
			break
		c1+=1
	nnt = f'x1/{nnt}'
	return nnt


def getSpot(t):
	c1 = 0
	c2 = 0
	m = []
	s = []
	at = t
	for i in t:
		if i == '/':
			s.append(c1)
			
			nt = t[c1+1:]
			for j in nt:
				if j=='/' or j =='+' or j =='-' or j =='x':
					s.append(c2+c1+1)
					s.append(subMub(at))
					at = nt
					break
				c2+=1
			c2 = 0

		c1+=1
		m.append(s)
		s = []
	m = [i for i in m if len(i) != 0]
	return m

def substr(b,e,t,r):
	nt = t[:b]+r+t[e:]
	return nt


print(getSpot(c))
rp = getSpot(c)

i = 0
print(c)
add = 0
for p in rp:
	c = substr(p[0]-add,p[1]+add,c,p[2])
	#print(p)
	add = 2
	i+=1 

print(c)