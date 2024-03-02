from machine import Pin, SPI
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))