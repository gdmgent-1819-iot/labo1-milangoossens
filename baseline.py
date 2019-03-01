import random
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

# random getal generator
def randNumb(endOfRange):
	return random.randint(0,endOfRange)

while(1):
	color1 = (randNumb(255),randNumb(255),randNumb(255))
	color2 = (randNumb(255),randNumb(255),randNumb(255))
	sense.show_message("Hello! We are New Media Development :)", text_colour=color1, back_colour=color2)
	


