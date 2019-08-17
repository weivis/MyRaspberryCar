# coding:utf-8
import RPi.GPIO as GPIO
import time

GPIO.cleanup()

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

# 电机旋转速度
leftMotor.ChangeDutyCycle(50)
rightMotor.ChangeDutyCycle(50)

GPIO.output(AIN1, True)
GPIO.output(AIN2, True)
GPIO.output(BIN1, True)
GPIO.output(BIN2, True)
time.sleep(3)

GPIO.cleanup()