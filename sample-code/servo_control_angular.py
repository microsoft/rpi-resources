# Import libraries
from gpiozero import AngularServo
from time import sleep

# Setup the max and min angle.
# Create the AngularServo object connected to pin 12
# Note: Please check the spec of your servo for the max angle and modify the following angle accordingly.
servo = AngularServo(12, min_angle=-100, max_angle=100)

# Continuously rotate servo between -100 deg, -50 deg, 0 deg,  50 deg and 100 deg.
while True:
    servo.angle = -100
    sleep(1)
    servo.angle = -50
    sleep(1)
    servo.angle = 0
    sleep(1)
    servo.angle = 50
    sleep(1)
    servo.angle = 100
    sleep(1)
    servo.angle = 50
    sleep(1)
    servo.angle = 0
    sleep(1)
    servo.angle = -50
    sleep(1)
