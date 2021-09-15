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
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
I didn't have any wiring for this asignment because I was using the neopixel on the board and no other components.

### Reflection
At first, I was very new to the circuit python. I didn't know how to even get started. But slowly but surely I used Mr. Dieroff's videos and learned how there isn't a void setup and loop anymore. The loop is called "while true instead." I finally got the code right and the board started printing blue. The problem was, I couldn't get in to print the other colors even though I told it to do so. With the help of Mr. H, I realized that my problem was the values of the print. Once I figured that out, I got it working.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
