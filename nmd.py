import random
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

# random getal generator
def randNumb(endOfRange):
	return random.randint(0,endOfRange)

# instelbare tekst
tekst = "NMD"

# instelbare tijd
tijd = 1  

while("true"):
	for i in tekst:
		color = (randNumb(255),randNumb(255),randNumb(255))
		sense.show_letter(str(i), text_colour= color)
		time.sleep(tijd)
	time.sleep(1)
