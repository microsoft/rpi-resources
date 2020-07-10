#Import Pi Camera and time libraries (built-in)
from picamera import PiCamera
from time import sleep

#Create a camera object
camera = PiCamera()
# Optional resolution setting
#camera.resolution = (480,640)

#Start camera
camera.start_preview(alpha=200)
sleep(5) #Recommended to wait 2s for light adjustment
# Optional rotation for camera
camera.rotation = 180
#Input image file path here
camera.capture('/home/pi/Desktop/image.jpg') 
#Stop camera
camera.stop_preview()