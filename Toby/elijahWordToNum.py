number={"one":1, "two":2, "three":3,  "four":4, "five":5,   "seven":7, "eight":8, "nine":9, "eleven":11, "twelve":12, "thirteen":13,"ten":10,  "six":6,"sixteen":16, "fourteen":14, "fifteen":15, "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20, "thirty":30,"forty":40, "fifty":50, "seventy":70,  "sixty":60,"eighty":80, "ninety":90}


multi={"hundred":100, "thousand":1000, "million":1000000, "billion":1000000000}	

multiplier=multi.keys()
digit=number.keys()

vot=[]
	

def word():
	numbers=input("type in a number in words to be converted:  ")
	nil=numbers.split()
	for wod in nil:
		if wod not in digit and wod not in multiplier:
			nil.remove(wod)
	return nil	



def iter(w):
	numba=0
	print(w)
	if len(w)>0:
		for i in range( len(w)):
			
			if w[i] in digit:
				numba=numba+number[w[i]]
				print(numba)
			
			elif w[i] in multiplier :
				numba=numba*multi[w[i]]
				print(numba)
				if len(w)-i>1 and w[i+1] in digit:
					vot.append(numba)
					w=w[(i+1):]
					i=0
					iter(w)
			
					
					
	vot.append(numba)					
	print(vot)
	
	
	
def converter():
	wo=word()
	iter(wo)
	print(vot)
converter()

