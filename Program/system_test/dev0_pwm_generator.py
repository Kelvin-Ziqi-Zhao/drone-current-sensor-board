from machine import Pin, PWM
import time

trig_master = Pin(18, Pin.OUT)
trig_master.value(0)

pwm0 = PWM(Pin(17),freq = 400, duty_ns = 1000000)
a = input("Waiting for start")

trig_master.value(1)
start = 1000000
end = 2000000
count = 10

ns = 900000
p = 1

while count > 0:
    ns = start
    while ns < end:
        time.sleep_us(10)
        ns = ns + 100*p
        pwm0.duty_ns(ns)
        
    time.sleep(0.5)
        
    ns = end
    while ns > start:
        time.sleep_us(10)
        ns = ns - 50*p
        pwm0.duty_ns(ns)
    
    count -= 1
    
    time.sleep(1)

print("Swap complete")

trig_master.value(0)