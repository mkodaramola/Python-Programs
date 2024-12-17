import subprocess
from time import sleep
import winsound


def getName(t):
	return t[t.find(':',0)+1:].strip()



mySearch = 'Ayeomoni Sunday FestusCAMON 17'


for j in range(500):
	result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
	result = result.decode('ascii').replace("\r","")
	networks = result.split("\n")

	networks = networks[4:]
	for i in range(len(networks)):
		if i == 0 or i%5 ==0:
			print(getName(networks[i]))
			if getName(networks[i]) == mySearch:
				winsound.Beep(2500,1000)

	print(j)
	sleep(2)

	
	



