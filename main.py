import serial
from serial import Serial

ser = serial.Serial("COM7", baudrate=9600, timeout=1)

while 1:
    arduinoData = ser.readline().decode()
    if arduinoData is not None:
        if arduinoData[0] == '[':
            print(arduinoData)
        else:
            continue

