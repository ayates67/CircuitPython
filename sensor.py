import adafruit_hcsr04
import time
import board
import neopixel
import simpleio
cm = 0

sdot = neopixel.NeoPixel(board.NEOPIXEL, 1)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D8, echo_pin=board.D9)
dot.brightness=0.1

while True:
    try:
        distance = sonar.distance
        print((distance,))

       print((sonar.distance,))
    if "distance >= 5" and "distance < 20":
        blue = int(simpleio.map_range(distance,5,20,0,255))
        green = (simpleio.map_range(distance,5,20,0,0))
        red = (simpleio.map_range(distance,5,20,255,0))

    if "distance >= 20" and "distance < 35":
        blue = int(simpleio.map_range(distance,5,20,0,255))
        green = int(simpleio.map_range(distance,5,20,0,0))
        red = int(simpleio.map_range(distance,5,20,255,0))
    print(red,green,blue)
        dot.fill((red, green, blue))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)