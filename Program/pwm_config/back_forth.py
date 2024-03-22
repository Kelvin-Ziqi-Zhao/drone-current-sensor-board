from machine import Pin, PWM
import time

pwm0 = PWM(Pin(17),freq = 400, duty_ns = 1000000)

ns = 1000000
p = 1
while(1):
    pwm0.duty_ns(ns)
    time.sleep_us(10)
    ns = ns + 10*p
    
    if ns == 2000000:
        p -= 2
        
    if ns == 1000000:
        p += 2