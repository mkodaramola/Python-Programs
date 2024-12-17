import keyboard
import pyautogui


#Screen width & height
scrWidth,scrHeight=pyautogui.size()
print("width:",scrWidth)
print("height:",scrHeight)

def myClick(x,y):
	rsw = 1366
	rsh = 768
	scrWidth,scrHeight=pyautogui.size()
	nx = (scrWidth * x)//1366
	ny = (scrHeight * y)//768
	pyautogui.click(nx,ny)
def myMoveTo(x,y):
	rsw = 1366
	rsh = 768
	scrWidth,scrHeight=pyautogui.size()
	nx = (scrWidth * x)//1366
	ny = (scrHeight * y)//768
	pyautogui.moveTo(nx,ny)




#mouse position
mX,mY = pyautogui.position()
print(mX,mY)



#move mouse

# pyautogui.moveTo(100,150,duration=1)
# pyautogui.click()
# pyautogui.moveRel(846,417,1)
#pyautogui.doubleClick()

#Scroll

#pyautogui.scroll(600,100,120)



#pyautogui.typewrite("enter")
#pyautogui.press("space")  

# pyautogui.FAILSAFE = False

# pyautogui.hotkey("ctrl","shift","esc")


# pyautogui.alert(text='Hello world',title="python",button='Yes')

#pyautogui.password("Enter name:",title="receive",mask="|")


def ResponsiveClick(x,y):
	rsw = 1366
	rsh = 768
	scrWidth,scrHeight=pyautogui.size()
	nx = (scrWidth * x)//1366
	ny = (scrHeight * y)//768
	pyautogui.click(nx,ny)

def myDrag(x,y):
	rsw = 1366
	rsh = 768
	scrWidth,scrHeight=pyautogui.size()
	nx = (scrWidth * x)//1366
	ny = (scrHeight * y)//768
	pyautogui.dragTo(nx,ny)


