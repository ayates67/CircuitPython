from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

start = time.monotonic()
max = 4
while True:
    photo = interrupter.value
    if photo and not state:
    state = photo
            counter += 1

    remaining = max - time.monotonic()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.monotonic() + 4
        counter = 0