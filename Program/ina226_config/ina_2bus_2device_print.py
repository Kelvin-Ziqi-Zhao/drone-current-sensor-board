import ina226
from time import sleep
from machine import Pin, I2C
# i2c
i2c = I2C(0,scl=Pin(9), sda=Pin(8))
# ina226
ina0 = ina226.INA226(i2c, 0x40)
ina1 = ina226.INA226(i2c, 0x41)
# default configuration and calibration value
ina0.set_calibration()
print(ina0.bus_voltage)
print(ina0.shunt_voltage)
print(ina0.current)
print(ina0.power)

ina1.set_calibration()
print(ina1.bus_voltage)
print(ina1.shunt_voltage)
print(ina1.current)
print(ina1.power)