import pyautogui
from PyDictionary import PyDictionary



def dFind(word):
		fob = open("dictionary.txt")
		t = fob.readlines()

		for i in range(len(t)):
			t[i] = t[i].lower()
			if(t[i][0:len(word)] == word):
				
				t[i]=t[i].replace(word,"",1)
				t[i]=t[i].replace("adj.","")
				t[i]=t[i].replace("—n","")
				t[i]=t[i].replace("—adv","")
				t[i]=t[i].replace("adv.","")
				t[i]=t[i].replace("—attrib.","")
				t[i]=t[i].replace("n.","")
				t[i]=t[i].replace(" v. "," ")
				t[i]=t[i].replace("—v.","in verb form,")
				t[i]=t[i].replace("—","")
				t[i]=t[i].replace("—s","in subject form")
				t[i]=t[i].replace("—int.","in interjection form")
				t[i]=t[i].replace("e.g","for example")
				t[i]=t[i].replace("pl.","in plural form")
				t[i]=t[i].replace("etc.","et cetera")
				t[i]=t[i].replace("colloq.","colloquial")
				if(t[i].count(".") >= 5):
					t[i] = t[0:fDot(t[i],5)]
				return t[i]
		return "NIL"
def fDot(text,pos):
		count = 0
		for i in range(len(text)):
			if(text[i] == "."):
				count += 1
			if count == pos:
				return i
def whats(t):
		if ("'s" in t):
			t = t[(t.find("'s")+3):len(t)]
		else:
			t = t[(t.find("is")+3):len(t)]
		t = t.replace("meaning of","",1)
		t = t.replace("does","",1)
		t = t.replace("the word","",1)
		t = t.replace("an ","",1)
		t = t.replace("a ","",1)
		t = t.replace("your ","",1)
		t = t.replace("the ","",1)
		t = t.replace("your ","",1)
		return t.strip().lower()

print(dFind(whats("what is a fun")))


def fDot(text,pos):
	count = 0
	for i in range(len(text)):
		if(text[i] == "."):
			count += 1
		if count == pos:
			return i




