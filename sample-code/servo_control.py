# Note: Use an external power supply to power a servo or other motor with the Pi as
#   the GPIO pins can only output max 50mA of current, while most motors need 100mA 
#   or more. This applies to any version of the Raspberry Pi.

# Import libraries
from gpiozero import Servo
from time import sleep

#Create a servo object connected to GPIO pin 17
servo = Servo(17)

#Continuously rotate servo between min, middle, and max locations
while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)