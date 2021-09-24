# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
The import board and neopixel and time are the variable that help the computer know what to do. Then I printed (make it red then green then blue.) The number in the dot fill tell the metro what color to print at a certain time.

Here's how you make code look like code:

```
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

while True:
    print("Make it red!")
    dot.fill((255, 0, 0))
    time.sleep(0.5)
    print("Make it green!")
    dot.fill((0, 255, 0))
    time.sleep(0.5)
    print("Make it cyan!")
    dot.fill((0, 128, 128))
    time.sleep(0.5)

```


### Evidence
![WIN_20210917_09_35_22_Pro_SparkVideo](https://user-images.githubusercontent.com/71342169/133791654-12184243-ffa3-44f9-a86e-33bec43fe039.gif)


### Wiring
I didn't have any wiring for this asignment because I was using the neopixel on the board and no other components.

### Reflection
At first, I was very new to the circuit python. I didn't know how to even get started. But slowly but surely I used Mr. Dieroff's videos and learned how there isn't a void setup and loop anymore. The loop is called "while true instead." I finally got the code right and the board started printing blue. The problem was, I couldn't get in to print the other colors even though I told it to do so. With the help of Mr. H, I realized that my problem was the values of the print. Once I figured that out, I got it working.




## CircuitPython_Servo

### Description & Code
The imports tell the computer what components I am working with. Then the adafruit motor tell the metro that I am using a motor and it also tell it how the motor works. Then the while true consists of the angle that the servo will move. It tells the servo to move back and fourth 180 degrees.
```
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):   # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```

### Evidence
![WIN_20210915_09_44_09_Pro_SparkVideo](https://user-images.githubusercontent.com/71342169/133789362-035773ec-70c5-427e-bfe7-5f5742c084d7.gif)

### Wiring
<img src="tinker servo.PNG">

### Reflection
This asignment was easier for me because I was more used to circuitpython going into it. One challenge I had was the wiring. I didn't know which wire went where. Luckily, I figuired it out by asking a few of my classmates and them helping me out. Then I googled a code for this asignment and found the perfect one. Once I got the wiring right, I got the servo up and running.



## CircuitPython_Distance Sensor

### Description & Code

```python
Code goes here

```

### Evidence
![WIN_20210924_09_28_54_Pro_SparkVideo (3)](https://user-images.githubusercontent.com/71342169/134684129-689edc3b-d5b2-4c37-8561-a209d757047c.gif)

### Wiring
<img src="tinker sensor.PNG">
### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
