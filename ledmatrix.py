import RPi.GPIO as GPIO
import time

def ledon(pin):
    GPIO.output(pin,GPIO.HIGH)
def ledoff(pin):
    GPIO.output(pin,GPIO.LOW)
def ledTick(pin,speed):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    time.sleep(speed)
    GPIO.setup(pin, GPIO.IN)
    time.sleep(speed)
    return

def init(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    return

def initialize():
    init(11)
    init(13)
    init(15)
    init(7)
    init(12)
    init(16)
    init(18)
    init(22)
    init(3)
    
def ledOrder(time):
  ledTick(11,time)
  ledTick(13,time)
  ledTick(15,time)
  ledTick(7,time)
  ledTick(12,time)
  ledTick(16,time)
  ledTick(18,time)
  ledTick(22,time)
  ledTick(3,time)

def ledOrderR(time):
    ledTick(3,time)
    ledTick(22,time)
    ledTick(18,time)
    ledTick(16,time)
    ledTick(12,time)
    ledTick(7,time)
    ledTick(15,time)
    ledTick(13,time)
    ledTick(11,time)

def spiral(time):
    ledTick(11,time)
    ledTick(13,time)
    ledTick(15,time)
    ledTick(16,time)
    ledTick(3,time)
    ledTick(22,time)
    ledTick(18,time)
    ledTick(7,time)

while True:
    initialize()
    spiral(.05)
    spiral(.05)
    ledOrder(.04)
    ledOrderR(.05)

