import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

O = [0, 0, 0] # wit
X = [255, 0, 0]  # Red
R = [255, 192, 203]  # roze
Y = [150, 75, 0]  # bruin
Z = [0, 0, 255]  # blauw

def marioNormal():
	
	mario = [
	O, O, O, X, X, O, O, O,
	O, O, X, X, X, X, X, O,
	O, O, O, R, Y, O, O, O,
	O, O, O, R, R, O, O, O,
	O, O, X, Z, Z, X, O, O,
	O, X, X, Z, Z, X, X, O,
	O, O, Z, Z, Z, Z, O, O,
	O, Y, Y, O, O, Y, Y, O
	]
	sense.set_pixels(mario)
	
def marioJump():
	
	mario = [
	O, O, X, X, X, X, X, O,
	O, O, O, R, Y, O, O, O,
	O, O, O, R, R, O, X, O,
	O, X, X, Z, Z, X, X, O,
	O, O, X, Z, Z, X, O, O,
	O, Y, Z, Z, Z, Z, Y, Y,
	Y, Y, Y, O, O, Y, Y, O,
	O, O, O, O, O, O, O, O
	]
	sense.set_pixels(mario)

while(1):
	marioNormal()
	event = sense.stick.wait_for_event()
	marioJump()
	time.sleep(0.2)
			




