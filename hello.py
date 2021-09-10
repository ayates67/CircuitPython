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
