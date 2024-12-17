class math:
	def textToNum(t):

		def ttd(t):
			teens = {'thir':13,'four':14,'fif':15,'six':16,'seven':17,'eight':18,'nine':19}
			tys = {'twen':20,'thir':30,'four':40,'fif':50,'six':60,'seven':70,'eight':80,'nine':90}
			units = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'hundred':0}


			if "eighty" in t:
				t = t.replace('ty', 't')
				t= t.strip()
				t = t.lower()
				dkeys = list(tys.keys())
				dvalues = list(tys.values())
				for i in range(len(tys)):
					if t == dkeys[i]:
						return dvalues[i]
			elif "eighteen" in t:
				t = t.replace('teen', 't')
				t= t.strip()
				t = t.lower()
				dkeys = list(teens.keys())
				dvalues = list(teens.values())
				for i in range(len(teens)):
					if t == dkeys[i]:
						return dvalues[i]
			elif "teen" in t:
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
		print (arr)
		f_sum = [0]*4
		ff_sum = 0
		for i in range(4):
			if arr[i] == '':
				continue
			else:
				f_sum[i] = toNum(arr[i])
				if i == 0:
					f_sum[i]*=1000000000
					
				if i == 1:
					f_sum[i]*=1000000
				
				if i == 2:
					f_sum[i]*=1000

		for i in range(4):
			ff_sum+=f_sum[i]



		return ff_sum





	def Mathswhats(t):
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
			if "division" in t:
				t = t.replace("division","",1)
				t = t.replace("of","",1)
				t = t.replace("by","divided",1)
			elif "multiplication" in t:
				t = t.replace(" multiplication ","",1)
				t = t.replace("by","times",1)
				t = t.replace("of","",1)

			t = t.replace('multiply by','times')
			t = t.replace('divided by','divided')
			sp = t.split(' ')
			temp = ""
			nsp = [None]*20
			ni = 0
			for i in range(len(sp)):
				if sp[i] == 'times':
					nsp[ni] = temp.strip() + '*'
					ni+=1
					temp = ""
				elif sp[i] == 'divided':
					nsp[ni] = temp.strip()+'/'
					ni+=1
					temp = ""
				elif sp[i] == 'plus':
					nsp[ni] = temp.strip() + '+'
					ni+=1
					temp = ""
				elif sp[i] == 'minus':
					nsp[ni] = temp.strip() + '-'
					ni+=1
					temp = ""
				else:
					temp += sp[i]
					temp += " "
			nsp[ni] = temp.strip()
					
			while None in nsp:
				nsp.remove(None)
			ftext = ""
			for v in nsp:
				if '*' in v:
					v = v.replace('*','')
					ftext += str(math.textToNum(v))
					ftext += '*'
				elif '/' in v:
					v = v.replace('/','')
					ftext += str(math.textToNum(v))
					ftext += '/'
				elif '+' in v:
					v = v.replace('+','')
					ftext += str(math.textToNum(v))
					ftext += '+'
				elif '-' in v:
					v = v.replace('-','')
					ftext += str(math.textToNum(v))
					ftext += '-'
			ftext += str(math.textToNum(nsp[-1]))

			print(ftext)



			


			return eval(ftext)



	def dmath(t):
		s = None
		if 'divide ' in t and ' by ' in t:
			t = t[t.find('divide')+7:len(t)]
			sp = t.split(' by ')
			s = math.textToNum(sp[0])
			for i in range(1,len(sp)):
				s/=math.textToNum(sp[i])

		elif 'multiply ' in t and ' by ' in t:
			t = t[t.find('multiply')+9:len(t)]
			sp = t.split(' by ')
			s = 1
			for i in range(len(sp)):
				s*=math.textToNum(sp[i])

		elif 'add ' in t and ' to ' in t:
			t = t[t.find('add')+4:len(t)]
			sp = t.split(' to ')
			s = 0
			for i in range(len(sp)):
				s+=math.textToNum(sp[i])

		elif 'subtract ' in t and ' from ' in t:
			t = t[t.find('subtract')+9:len(t)]
			sp = t.split(' from ')
			s = math.textToNum(sp[0])
			for i in range(1,len(sp)):
				s-=math.textToNum(sp[-i])
			s *=-1



		return s



	def WhatSumm(t):
		t= t[t.find('sum'):len(t)]
		t = t[t.find('of')+3:len(t)]
		t = t.replace(',','')
		arr = t.split(' ')
		s = 0
		for i in arr:
			if i == 'and':
				continue
			s += math.textToNum(i)

		return s

	def whatsText(t):
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
			return t.strip().lower()



	def que(text):
		text = text.lower()
		if (("what is" in text or "what's" in text) and ('sum' in text) and ('of' in text)):
				ans = math.WhatSumm(text)
				return (f"{math.whatsText(text)} is {ans}")
		elif(("what is" in text or "what's" in text) and ('times' in text or 'multiply' in text or 'divide' in text or 'plus' in text or 'minus' in text or 'add' in text or 'substract' in text)):
				ans = math.Mathswhats(text)
				return f"{math.whatsText(text)} is equal to  {ans}"
		elif ('substract' in text and 'from' in text) or ('add' in text and 'to' in text) or ('multipl' in text and 'by' in text) or ('divide' in text and 'by' in text):
				ans = math.dmath(text)
				return f'The answer is {ans}'
		else:
			return "Null"




print(math.que("three thousand multiplied by the sum of 5 and 0.55"))







