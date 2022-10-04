import serial
import time
import sys


class RLC:
    def __init__(self,ser=0):
        print "Start connection with RLC 300 meter"
        self.ser = serial.Serial(ser,baudrate=9600,stopbits=serial.STOPBITS_ONE,timeout=2)
        print "Connection with  RLC 300 meter OK at serial port",ser
        self.ser.write(chr(20)+chr(9)+chr(25))
        self.ser.write("*RST;*CLS\n")
        
    def __del__(self):
        self.ser.close()

if __name__ == "__main__":

    rlc = RLC()
    print rlc.__del__()

     
 


   

    



