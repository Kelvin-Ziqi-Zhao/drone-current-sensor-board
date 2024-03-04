from machine import Pin, SPI
import machine
import os
import winbond

spi = SPI(0, baudrate=2000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
cs = machine.Pin(5, machine.Pin.OUT)
cs.high()

cs.low()
data = spi.read(4)
cs.high()

print(data)

'''
flash = winbond.W25QFlash(spi=spi0,
                          cs=Pin(5),
                          baud=2000000,
                          software_reset=True)

'''