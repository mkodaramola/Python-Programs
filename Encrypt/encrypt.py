# ord('a') = 97
# chr(97) = a
import random

def Encrypt(fn):
	try:
		file =open(fn,'r')
		text = file.read()
		file.close()
		if text[0:3] != ">|<":
			fe = ""
			etxt = ""
			netxt = ""
			for i in text:
				e = bin(ord(i))
				e = e.replace('0b','')
				e = list(e)
				while len(e) < 8:
					e.insert(0,'0')
				for j in e:
					fe +=j
				etxt += fe
				fe = ""

			for i in etxt:
				
				if (i == '0'):
					r = random.randint(0,5)
					if r == 0:
						i = "#"
					elif r == 1:
						i = "%"
					elif r == 2:
						i = "!"
					elif r == 3:
						i = "<"
					elif r == 4:
						i = "~"
					else:
						i = "&"
				elif (i == '1'):
					r = random.randint(0,5)
					if r == 0:
						i = "*"
					elif r == 1:
						i = "^"
					elif r == 2:
						i = "$"
					elif r == 3:
						i = "@"
					elif r == 4:
						i = "("
					else:
						i = "?"
				netxt += i

			netxt = netxt.replace("",">|<",1)

			wf = open('enf.txt','w')
			wf.write(netxt)
			wf.close()
			print("Encryption Complete!")

		else:
			print("File Already Encrypted!")

	except:
		print("Failed to Encrypt!")


	

def Decrypt(fn):
	try:

		file =open(fn,'r')
		bin = file.read()
		file.close()
		if bin[0:3] == ">|<":

			bin = bin.replace(">|<","",1)
			deBin = ""
			for i in bin:
				if i == '#' or i =='%' or i =='!' or i =='&' or i == '<' or i =='~':
					i = '0'
				elif i == '*' or i =='^' or i =='$' or i =='?' or i =='@' or i =='(':
					i = '1'
				deBin += i

			b = ""
			bl = []
			text = ""
			ct = 0
			for i in deBin:
				b+= i
				ct +=1
				if ct % 8 == 0:
					bl.append(chr(int(b,2)))
					b = ""
			wf = open(fn,'w')
			wf.write(text.join(bl))
			wf.close()
			print("Decryption Complete!")
		else:
			print("File Already Decrypted!")
	except:
		print("Failed to Decrypt")







Decrypt('enf.txt')

