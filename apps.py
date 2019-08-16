# coding:utf-8
import RPi.GPIO as GPIO
import time

def forward(speed,runtime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, True)#AIN1高电平则正转
    GPIO.output(AIN2, False)#如果为True则翻转
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)
    time.sleep(runtime)

def backword(speed, backtime):
      leftMotor.ChangeDutyCycle(speed)
      GPIO.output(AIN2, True)  # AIN2
      GPIO.output(AIN1, False)  # AIN1
      rightMotor.ChangeDutyCycle(speed)
      GPIO.output(BIN2, True)  # BIN2
      GPIO.output(BIN1, False)  # BIN1
      time.sleep(backtime)

def turnLeft(speed, lefttime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, True)
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)
    time.sleep(lefttime)

#右转弯函数
def turnRight(speed, righttime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, True)
    GPIO.output(AIN2, False)
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, True)
    time.sleep(righttime)

if __name__ == '__main__':
    try:
         while True:
             forward(50,3)
             turnLeft(70, 3)
             backword(50,3)
             turnRight(70,3)
    except KeyboardInterrupt:
         GPIO.cleanup()