# Raspberry Pi Sample Code

This folder contains example Python code to use the Pi Camera and General Purpose Input and Output (GPIO) pins. To use the code samples:
1. Download the code samples onto your Raspberry Pi.
1. Follow the wiring diagrams in the [schematics folder](./schematics).
1. Download code libraries using pip. For example:
``` sudo pip install gpiozero ```
1. Open the code sample in your preferred Python editor 
1. Make any required updates as indicated in the code sample comments.
1. Run the program!
    * Run the sample programs with Python3:  ```sudo python3 program_name.py ```

## Contents
* [Sample Python programs with the GPIO Zero library (e.g. blink an LED, pushbutton input, and more)](https://gpiozero.readthedocs.io/en/stable/recipes.html)
* [Image Capture with the Pi Camera in Python (Raspberry Pi Foundation)](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4)
* Pi Camera Image Capture with a Pushbutton: [pushbutton_image_capture.py](pushbutton_image_capture.py)
* Pi Servo Control: 
    * [servo_control.py](servo_control.py)
    * [servo_control_angular.py](servo_control_angular.py)  
    Note: Please check the spec of your servo for the max angle and modify the max/min angles in the code accordingly.
    * [servo_control_noJitter.py](servo_control_noJitter.py)  
    Note: You will need to install a library before running the example  
    ```sudo pip3 pigpio```  
    Before you run the code, please run the following command in terminal first  
    ```sudo pigpiod```
 

## Wiring Diagrams
Check the [schematics](./schematics) folder for wiring diagrams for relevant examples.

*All schematics were made with [Fritzing](https://fritzing.org/).*

## Resources and Going Forward
### Beginner Resources
All of the following resources are created and maintained by the [Raspberry Pi Foundation](https://www.raspberrypi.org/).
* [Python Coding on the Pi](https://www.raspberrypi.org/documentation/usage/python/README.md)
* [GPIO overview ](https://www.raspberrypi.org/documentation/usage/gpio/)
* [Assorted projects and guides](https://projects.raspberrypi.org/en)

### Intermediate and Advanced Resources
* [GPIO Zero Library Documentation](https://gpiozero.readthedocs.io/en/stable/)
* [Pi Camera Library Documentation](https://picamera.readthedocs.io/en/release-1.13/)
* [Assorted Azure Learning Resources](https://docs.microsoft.com/en-us/learn/azure/)

### Jitter Free Servo Resources
* [Jitter Free Servo Control on the Raspberry Pi](https://steemit.com/python/@makerhacks/jitter-free-servo-control-on-the-raspberry-pi)
* [Raspberry Pi Servo Jitter](https://ben.akrin.com/?p=9158)

## Contributions? Questions? Requests?
As mentioned in the main README, we welcome contributions! Please read through the README and Code of Conduct to submit a pull request.

Please open an issue if you have questions or requests!
