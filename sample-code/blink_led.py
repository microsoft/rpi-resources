#                     Blink LED                     
# Sample code showing how to use GPIO library

#import Pi GPIO library button class
from gpiozero import LED   # From the Raspberry Pi GPIO library import LED
from time import sleep     #Import the sleep function from the time module

# Define LEDs and GPIO pin numbers
# --> Change GPIO pins as needed
led = LED(17)

#Create a forever loop to blink the LED on and off
while True:
    led.on() # Turn LED on
    sleep(1) # Sleep for 1 second
    led.off() # Turn LED off
    sleep(1) # Sleep for 1 second