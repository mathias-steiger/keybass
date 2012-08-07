#!/usr/bin/env python 
## Play deep bass (or any wav file) on keypresses in Linux
## 10% of the code is from somewhere I can't remember
## GLP License

from Xlib.display import Display 
import threading, time, os, copy

done = 0 

class play_sound1(threading.Thread):
	def run(self):
		global done
		try:
			os.system("aplay bass.wav")
		except (KeyboardInterrupt, SystemExit):
			done = 1


class play_sound2(threading.Thread):
	def run(self):
		global done
		try:
			os.system("aplay bass.wav")
		except (KeyboardInterrupt, SystemExit):
			done = 1

class play_sound3(threading.Thread):
	def run(self):
		global done
		try:
			os.system("aplay bass.wav")
		except (KeyboardInterrupt, SystemExit):
			done = 1

def main():
	try:
		global done
		lastkeys = {}
		counter = 0
		disp = Display()
		while done == 0:
			keymap = disp.query_keymap()
			if len(keymap)==len(lastkeys) and (any(keymap[i] > lastkeys[i] for i in range(len(keymap)-1))):
				if counter%3 == 0: 
					play_sound1().start()
				elif counter%3 == 1: 
					play_sound2().start()
				elif counter%3 == 2: 
					play_sound3().start()
				counter = (counter+1)%1000;
			lastkeys = keymap
			time.sleep(0.01)
	except (KeyboardInterrupt, SystemExit):
		done = 1
if __name__ == '__main__': 
	main()
