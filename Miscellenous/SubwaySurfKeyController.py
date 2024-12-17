from pynput import keyboard
from threading import Thread


def onPress(key):
	try:
		print(f'{key.char}')
	except AttributeError:
		print(f'{key}')

def onRelease(key):
	print(f"{key} Released")
	if (key == keyboard.Key.esc):
		return False





with keyboard.Listener(on_press = onPress,on_release = onRelease) as listener:
	listener.join()


	