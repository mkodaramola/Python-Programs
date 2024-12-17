import pyautogui as pa
from time import sleep


pa.hotkey('winleft','e')

sleep(3)

music = pa.locateCenterOnScreen("music.png")
pa.doubleClick(music)

sleep(2)

songs = pa.locateCenterOnScreen("mysong.png")
pa.doubleClick(songs)


sleep(1)

praise = pa.locateCenterOnScreen("praise.png")
pa.click(praise,button='right')


sleep(1)

play = pa.locateCenterOnScreen("play.png")
pa.click(play)












