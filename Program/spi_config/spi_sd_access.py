from machine import Pin, SPI
import machine, sdcard, os

spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
sd = sdcard.SDCard(spi, Pin(1))

os.mount(sd, '/sd')
with open("/sd/test.txt", "w") as f:
    f.write("Hello world!\r\n")