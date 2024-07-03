from machine import Pin
import tome
digital = Pin(18, Pin.IN)

while True:
    print (str(digital.value()))
    time.sleep(2)