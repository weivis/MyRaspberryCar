# coding:utf-8
import RPi.GPIO as GPIO
import time

# 绑定对应的引脚，来自于图纸
PWMA = 18
AIN1 = 22
AIN2 = 27
PWMB = 23
BIN1 = 25
BIN2 = 24
# 超声波引脚
TRIG = 20
ECHO = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# 设置引脚为输出

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
# 电机
leftMotor = GPIO.PWM(PWMA, 100)
rightMotor = GPIO.PWM(PWMB, 100)
leftMotor.start(0)
rightMotor.start(0)



##小车的前进函数
def forward(speed, runtime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, True)  # AIN1高电平则正转
    GPIO.output(AIN2, False)  # 如果为True则翻转
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)
    time.sleep(runtime)  # 维持状态的时间，如果不给命令执行其他，将会继续执行


# 后退函数
def backword(speed, backtime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)
    GPIO.output(AIN1, False)
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)
    GPIO.output(BIN1, False)
    time.sleep(backtime)


# 左转弯函数
def turnLeft(speed, lefttime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, False)
    GPIO.output(AIN2, True)
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, True)
    GPIO.output(BIN2, False)
    time.sleep(lefttime)


# 右转弯函数
def turnRight(speed, righttime):
    leftMotor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, True)
    GPIO.output(AIN2, False)
    rightMotor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, False)
    GPIO.output(BIN2, True)
    time.sleep(righttime)

# 超声波测距函数
def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    while GPIO.input(ECHO) == 0:
        pass
    emitTime = time.time()
    while GPIO.input(ECHO) == 1:
        pass
    acceptTime = time.time()
    totalTime = acceptTime - emitTime
    distanceForReturn = totalTime * 340 / 2 * 100
    return  distanceForReturn
def loop():
    while True:
        dis= distance()
        if dis<50:
            while dis<50:
                backword(50, 0.2)
                dis=distance()
        else:
            forward(50, 0)


if __name__ == '__main__':
    try:
        forward(50, 0)
        loop()

    except KeyboardInterrupt:
        GPIO.cleanup()