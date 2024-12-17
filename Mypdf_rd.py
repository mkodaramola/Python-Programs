import PyPDF2 as pdf


allQ = ""
ent = open('fl.pdf','rb')
pdfReader = pdf.PdfFileReader(ent)

#print(pdfReader.numPages)

chp = input("Chapter: ")
chp = chp.lower()

if chp == "1":
        r1 = 7
        r2 = 14
elif chp == '2':
        r1 = 14
        r2 = 19
elif chp == '3':
        r1 = 19
        r2 = 23
elif chp == '4':
        r1 = 23
        r2 = 25
elif chp == '5':
        r1 = 25
        
        r2 = 30
elif chp == '9':
        r1 = 39
        r2 = 44
elif chp == '10a':
        r1 = 44
        r2 = 47
elif chp == '10b':
        r1 = 47
        r2 = 50
elif chp == '12':
        r1 = 53
        r2 = 56
elif chp == '13':
        r1 = 56
        r2 = 61
else:
        r1= 7
        r2 = 14
        chp = 1
       

for i in range(r1,r2):
	pageO = pdfReader.getPage(i)
	allQ += pageO.extractText()
ent.close()


for i in range(1,102):
	bq = allQ.find(str(i)+".")
	if (i <= 60 and chp == '1') or chp == '9':
		eq = allQ.find('Ans')
	else:
		eq = allQ.find('(')

   	 	 
	disp = allQ[bq:eq]
	print(disp)
	ba = eq
	ea = allQ.find(str(i+1)+".")
	userA = input(">")
	dispA = allQ[ba:ea]
	bta = dispA.find('(')
	eta = dispA.find(')')   
	print(dispA)
        
	           
	allQ = allQ[allQ.find(str(i+1)+"."):]
