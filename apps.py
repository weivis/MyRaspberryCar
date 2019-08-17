# coding:utf-8
import RPi.GPIO as GPIO
import time

'''18引脚控制的是左侧两个电机'''
PWMA = 18
'''23引脚控制的右侧两个电机'''
PWMB = 23

'''AIN1、AIN2、BIN1、BIN2控制的是左右两侧电机的正转和翻转'''
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

'''设置引脚为输出'''
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

#电机
leftMotor = GPIO.PWM(PWMA, 100)
rightMotor = GPIO.PWM(PWMB, 100)
leftMotor.start(0)
rightMotor.start(0)

def forward(speed, backtime):
    print('前进')
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)  # AIN2
    GPIO.output(AIN1, False)  # AIN1
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(backtime)


def backword(speed, backtime):
    print('后退')
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)  # AIN2
    GPIO.output(AIN1, False)  # AIN1
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)  # BIN2
    GPIO.output(BIN1, False)  # BIN1
    time.sleep(backtime)

#左转弯函数
def turnLeft(speed, lefttime):
    print('左转向')
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, True)
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)
    time.sleep(lefttime)

def turnRight(speed, righttime):
    print('右转向')
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
             # forward(50,3)
             turnLeft(70, 3)
             # backword(50,3)
             # turnRight(70,3)
    except KeyboardInterrupt:
         GPIO.cleanup()