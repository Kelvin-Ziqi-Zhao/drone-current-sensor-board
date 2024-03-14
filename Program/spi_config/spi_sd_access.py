from machine import Pin, SPI
import machine, sdcard, os
import time

spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
sd = sdcard.SDCard(spi, Pin(1))

os.mount(sd, '/sd')
count = 0
start = time.ticks_ms()
with open("/sd/test.txt", "w") as f:
    while(count<10000):
        sdstart = time.ticks_ms()
        count += 1
        f.write(str(count))
        print(count)
        f.write("\r\n")
        while time.ticks_diff(time.ticks_ms(), sdstart) < 10:
            time.sleep_us(1)
    
delta = time.ticks_diff(time.ticks_ms(), start)
print(delta)
    