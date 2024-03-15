import ina226
import time
from machine import Pin, I2C
# i2c
i2c = I2C(0,scl=Pin(9), sda=Pin(8))
# ina226
ina0 = ina226.INA226(i2c, 0x40)
ina1 = ina226.INA226(i2c, 0x41)
# default configuration and calibration value
ina0.set_calibration()
ina1.set_calibration()
while(1):
    print("bus_voltage  ",ina0.bus_voltage,ina1.bus_voltage)
    print("shunt_voltage",ina0.shunt_voltage,ina1.shunt_voltage)
    print("current      ",ina0.current,ina1.current)
    print("power        ",ina0.power,ina1.power)
    time.sleep(0.02)
