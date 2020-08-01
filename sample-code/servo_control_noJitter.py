# You might see jitter when control the Servo.
# This example shows how you can get rid of the jitter.
# To understand more, see the reference below:
# Reference: https://steemit.com/python/@makerhacks/jitter-free-servo-control-on-the-raspberry-pi
#            https://ben.akrin.com/?p=9158


# Note: You will need to install a library before running the example
# > sudo pip3 pigpio

# Before you run the code, please run the following command first
# > sudo pigpiod

# Import libraries
import pigpio
from time import sleep

# Config the servo with pin 12
servo = 12
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo, 50)

# Continuously rotate servo between 0 deg, 90 deg, 180 deg.
while True:
    # 0 deg
    pwm.set_servo_pulsewidth(servo, 500)
    sleep(1)
    # 90 deg
    pwm.set_servo_pulsewidth(servo, 1500)
    sleep(1)
    # 180 deg
    pwm.set_servo_pulsewidth(servo, 2500)
    sleep(1)