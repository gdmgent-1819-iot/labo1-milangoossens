import time
import random
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

# random getal generator
def randNumb(endOfRange):
	return random.randint(0,endOfRange)

# op hoeveel seconden wil je alle pixels doorlopen?
tijd1 = 10

def easeTime(tijd):
	return tijd/64.0

while("true"):
	for y in range(0,8):
		for i in range(0,8):
			color = (randNumb(255),randNumb(255),randNumb(255))
			sense.set_pixel(i,y,color)
			time.sleep(easeTime(tijd1))
			sense.set_pixel(i,y,0,0,0)
	
	
	
