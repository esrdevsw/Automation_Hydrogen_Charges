import serial
import time
import sys


class RLC:
    def __init__(self,ser=0):
        self.ser = serial.Serial(ser,baudrate=9600,stopbits=serial.STOPBITS_ONE,timeout=2)
##        self.ser.write(chr(20)+chr(9)+chr(25))
##        self.ser.write("*RST;*CLS\n")
        
    def read_c(self):
        time.sleep(0.5)
        self.ser.write("FREQ 10000; LEVEL_LOW; ACIRC_OFF\n")
        self.ser.write("ACIRC_OFF\n")
        self.ser.write("CIRC_SER\n")
##        self.ser.write("AVG 10\n")
        self.ser.write("MODE_CR;MON_VI\n")
        self.ser.write("*TRG;C?; R?; MON_V? ; MON_I?\n")     
        answer = self.ser.readline()

        try:
            s = answer.split(';')
            return (s)
        except:
            return "ERROR"
        
        
    def __del__(self):
        self.ser.write(chr(20))
        self.ser.write("*CLS\n")
        self.ser.close()

		
if __name__ == "__main__":

    rlc = RLC()
##    for n in range(10):

    print time.strftime('%X '), time.strftime('%x '), rlc.read_c()
   
    del(rlc)

