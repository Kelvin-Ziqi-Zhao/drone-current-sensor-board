from machine import Pin, PWM
import time

pwm0 = PWM(Pin(17),freq = 400, duty_ns = 1000000)
a = input()
start = 1000000
end = 2000000

ns = 900000
p = 1
while(1):
    ns = start
    while ns < end:
        time.sleep_us(10)
        ns = ns + 10*p
        pwm0.duty_ns(ns)
        
    ns = end
    while ns > start:
        time.sleep_us(10)
        ns = ns - 10*p
        pwm0.duty_ns(ns)