import serial
import time

timeStamp = time.time()
ser = serial.Serial("/dev/ttyACM0", 9600)
count = 0
records = []

while count < 3:
    records.append(ser.readline())
    count += 1

theDate = time.strftime("%Y_%m_%d")
serialDataFile = theDate + "_seed_starter_temps"
with open(serialDataFile, 'a') as outFile:
    if records[1] >= 75:
        outFile.write(str(timeStamp) + "," + records[1])
    elif records[2] >= 75:
        outFile.write(str(timeStamp) + "," + records[2])
    
