import serial
import time

timeStamp = time.time()
ser = serial.Serial("/dev/ttyACM0", 9600)
count = 0
records = []

while count < 3:
    records.append(ser.readline())
    count += 1

with open("serialTest.txt", 'a') as outFile:
    if records[1] >= 75:
        outFile.write(str(timeStamp) + "," + records[1])
    
