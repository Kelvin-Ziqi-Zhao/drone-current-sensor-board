import ina226
import time,sys
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# i2c
i2c = I2C(0,scl=Pin(9), sda=Pin(8))
# ina226
ina0 = ina226.INA226(i2c, 0x40)
ina1 = ina226.INA226(i2c, 0x41)
# default configuration and calibration value
ina0.set_calibration()
ina1.set_calibration()
    
# ssd1306
pix_res_x  = 128 # SSD1306 horizontal resolution
pix_res_y = 64   # SSD1306 vertical resolution

i2c_dev = I2C(1,scl=Pin(7),sda=Pin(6),freq=200000)  # start I2C on I2C1 (GPIO 26/27)
i2c_addr = [hex(ii) for ii in i2c_dev.scan()] # get I2C address in hex format
if i2c_addr==[]:
    print('No I2C Display Found') 
    sys.exit() # exit routine if no dev found
else:
    print("I2C Address      : {}".format(i2c_addr[0])) # I2C device address
    print("I2C Configuration: {}".format(i2c_dev)) # print I2C params

oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev) # oled controller
oled.fill(0)

while(1):
    oled.text("Power Monitor",0,5)
    oled.text("Vbus:",0,15)
    oled.text("I0:",0,25)
    oled.text("I1:",0,35)
    oled.text("P0:",0,45)
    oled.text("P1:",0,55)
    
    oled.text(str(ina0.bus_voltage)+"V",45,15)
    oled.text(str(ina0.current)+"A",45,25)
    oled.text(str(ina1.current)+"A",45,35)
    oled.text(str(ina0.power)+"W",45,45)
    oled.text(str(ina1.power)+"W",45,55)
    
    '''
    print("bus_voltage  ",ina0.bus_voltage,ina1.bus_voltage)
    print("shunt_voltage",ina0.shunt_voltage,ina1.shunt_voltage)
    print("current      ",ina0.current,ina1.current)
    print("power        ",ina0.power,ina1.power)
    '''
    
    oled.show()
    time.sleep_us(10)
    oled.fill(0)