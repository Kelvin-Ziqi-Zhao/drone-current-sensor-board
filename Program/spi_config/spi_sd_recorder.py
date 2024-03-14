from machine import Pin, SPI, I2C
import machine, sdcard, os
import time
import ina226

# sd card config
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
sd = sdcard.SDCard(spi, Pin(1))

os.mount(sd, '/sd')
count = 0


# ina226 config
i2c = I2C(0,scl=Pin(9), sda=Pin(8))

ina0 = ina226.INA226(i2c, 0x40)
ina1 = ina226.INA226(i2c, 0x41)
# default configuration and calibration value
ina0.set_calibration()
ina1.set_calibration()

start = time.ticks_ms()
with open("/sd/test.txt", "w") as f:
    f.write("time_ms,V0,V1,I0,I1,P0,P1\r\n")
    while(count<1000):
        sdstart = time.ticks_ms()
        count += 1
        t = time.ticks_diff(time.ticks_ms(), start)
        f.write(str(t))
        print(t)
        f.write(",")
        f.write(str(ina0.bus_voltage))
        print(ina0.bus_voltage)
        f.write(",")
        f.write(str(ina1.bus_voltage))
        f.write(",")
        f.write(str(ina0.current))
        f.write(",")
        f.write(str(ina1.current))
        f.write(",")
        f.write(str(ina0.power))
        f.write(",")
        f.write(str(ina1.power))
        f.write("\r\n")
        while time.ticks_diff(time.ticks_ms(), sdstart) < 10:
            time.sleep_us(1)
    
delta = time.ticks_diff(time.ticks_ms(), start)
print(delta)
    