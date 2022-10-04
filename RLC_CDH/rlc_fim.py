import serial
import time
import sys


class RLC:
    def __init__(self,ser=0):
        self.ser = serial.Serial(ser,baudrate=9600,stopbits=serial.STOPBITS_ONE,timeout=2)
        print "FIM DAS MEDIDAS"	
        self.ser.write(chr(20)+chr(25))
        self.ser.write("*RST;*CLS\n")
        self.ser.write(chr(1))
        

    def __del__(self):
        self.ser.close()
	
if __name__ == "__main__":

    rlc = RLC()
    print rlc.__del__()



               
