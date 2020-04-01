
import serial
import numpy as np
import serial.tools.list_ports
import time


def ardconnect():
    
    
    portName = ""
    str2 = ""
    
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if portName == '':    
            int1 = 0
            while int1 <= 20:   
                if "USB Serial Device" in p[1]:  
                    
                    str2 = str(int1) 
                    portName = "COM" + str2 
                    
                if "USB Serial Device" in p[1] and portName in p[1]: 
                    print("Found Sensor on " + portName)
                    break
                
                int1 = int1 + 1
                    
        else:
            break

    if portName == '':  
        raise IOError("No Sensor found")
    
    baudrate = 9600
    ser = serial.Serial(portName, baudrate)
    return ser
    
    





