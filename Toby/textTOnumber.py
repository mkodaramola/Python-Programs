def textToNum(t):

	def ttd(t):
		teens = {'thir':13,'four':14,'fif':15,'six':16,'seven':17,'eight':18,'nine':19}
		tys = {'twen':20,'thir':30,'four':40,'fif':50,'six':60,'seven':70,'eight':80,'nine':90}
		units = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'hundred':0}

		if "teen" in t:
			t = t.replace('teen', '')
			t= t.strip()
			t = t.lower()
			dkeys = list(teens.keys())
			dvalues = list(teens.values())
			for i in range(len(teens)):
				if t == dkeys[i]:
					return dvalues[i]
		elif t[-2:] == 'ty':
			t = t.replace('ty', '')
			t= t.strip()
			t = t.lower()
			dkeys = list(tys.keys())
			dvalues = list(tys.values())
			for i in range(len(tys)):
				if t == dkeys[i]:
					return dvalues[i]
		else:
			dkeys = list(units.keys())
			dvalues = list(units.values())
			for i in range(len(units)):
				if t == dkeys[i]:
					return dvalues[i]
	


	t = t.replace(',','')
	t = t.replace(' and','')
	num = 0

	def Analyse(t):
		b = ""
		m = ""
		th = ""
		h = ""

		if "billion" in t:
			b = t[0:t.find('billion')-1]
			t = t[t.find('billion')+8:len(t)]
		if "million" in t:
			m = t[0:t.find('million')-1]
			t = t[t.find('million')+8:len(t)]
		if "thousand" in t:
			th = t[0:t.find('thousand')-1]
			t = t[t.find('thousand')+9:len(t)]
		h = t


		return [b,m,th,h]


	def toNum(t):
		a = t.split(' ')
		s = 0
		temp=1
		for i in range(len(a)):
			num = ttd(a[i])
			if num == 0:
				s *= 100
			else:
				s+=num	
			
		return s


	arr = Analyse(t)
	f_sum = 0
	for i in range(4):
		if arr[i] == '':
			continue
		else:
			f_sum += toNum(arr[i])
			if i == 0:
				f_sum*=1000
			if i == 1:
				f_sum*=1000
			if i == 2:
				f_sum*=1000



	return f_sum

def whats(t):
		if ("'s" in t):
			t = t[(t.find("'s")+3):len(t)]
		elif (' is ' in t):
			t = t[(t.find("is")+3):len(t)]
		elif 'does it' in t:
			t = t[(t.find("does it")+8):len(t)]
		elif 'does' in t:
			t = t[(t.find("does")+5):len(t)]
		t = t.replace("meaning of","",1)
		t = t.replace("means","",-1)
		t = t.replace("mean","",-1)
		t = t.replace("an ","",1)
		t = t.replace("a ","",1)
		t = t.replace("your ","",1)
		t = t.replace("to be","",1)
		t = t.replace("to","",1)
		t = t.replace("the ","",1)
		t = t.replace("your ","",1)

		if 'plus' in t:
			s = 0
			sp = t.split(' plus ')
			for i in range(len(sp)):
				s+=textToNum(sp[i])
		elif 'times' in t:
			s = 1
			sp = t.split(' times ')
			for i in range(len(sp)):
				s*=textToNum(sp[i])
		elif 'multiply by' in t:
			s = 1
			sp = t.split(' multiply by ')
			for i in range(len(sp)):
				s*=textToNum(sp[i])

		elif 'divided by' in t:
			sp = t.split(' divided by ')
			s = textToNum(sp[0])
			for i in range(1,len(sp)):
				s/=textToNum(sp[i])

		elif 'subtracted by' in t:
			sp = t.split(' subtracted by ')
			s = textToNum(sp[0])
			for i in range(1,len(sp)):
				s-=textToNum(sp[i])

		elif 'minus' in t:
			sp = t.split(' minus ')
			s = textToNum(sp[0])
			for i in range(1,len(sp)):
				s-=textToNum(sp[i])


		return s


def dmath(t):
	if 'divide ' in t and ' by ' in t:
		t = t[t.find('divide')+7:len(t)]
		sp = t.split(' by ')
		s = textToNum(sp[0])
		for i in range(1,len(sp)):
			s/=textToNum(sp[i])

	elif 'multiply ' in t and ' by ' in t:
		t = t[t.find('multiply')+9:len(t)]
		sp = t.split(' by ')
		s = 1
		for i in range(len(sp)):
			s*=textToNum(sp[i])

	elif 'add ' in t and ' by ' in t:
		t = t.replace(' up ','')
		t = t.replace('together','')
		t = t[t.find('add')+4:len(t)]
		sp = t.split(' and ')
		s = 0
		print(sp)
		for i in range(len(sp)):
			s+=textToNum(sp[i])





	return s
print(whats("what is three minus five"))

print(dmath('Toby please add up eighteen and twelve together'))

