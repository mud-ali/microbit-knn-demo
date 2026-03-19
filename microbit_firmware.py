# Upload this code to the micro:bit

from microbit import *

display.clear()
display.set_pixel(2, 2, 9)

while True:
    temp = temperature()
    light = display.read_light_level()
    sound = microphone.sound_level()

    # Send data as CSV: "temp,light,sound"
    print(str(temp) + "," + str(light) + "," + str(sound))

    # continue sending data every 500ms
    sleep(500)
