import random
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

# kies de kleur van de avatars
color = (255,0,0)

# kies de tijd tussen de verschillende avatars (in seconden)
tijd = 2

# random getal generator
def randNumb(endOfRange):
	return random.randint(0,endOfRange)

while(1):
	for y in range(0,8):
		for i in range(0,4):
			state = randNumb(1)
			
			if state == 0:
				sense.set_pixel(i,y,0,0,0)
				sense.set_pixel(7-i,y,0,0,0)
			if state == 1:
				sense.set_pixel(i,y,color)
				sense.set_pixel(7-i,y,color)
			
	time.sleep(tijd)
		
			



