#!/usr/bin/env python
import os
import serial
import time
import popen2
import sys
import gnuplot

class RLC:
    def __init__(self,ser=2):
##        print "Start connection with RLC 300 meter"
        self.cnt = serial.Serial(ser,baudrate=9600,stopbits=serial.STOPBITS_ONE,timeout=2)
##        print "Connection with  counter OK at serial port",ser
        self.cnt.write(chr(20)+chr(9)+chr(25))
        self.cnt.write("*RST;*CLS\n")

    def read_vi(self):
        time.sleep(0.5)
        self.cnt.write("FREQ 1000;LEVEL_LOW\n")
        self.cnt.write("MODE_CD;MON_VI\n")
        self.cnt.write("*TRG;C?;MON_V?;MON_I?\n")
        answer = self.cnt.readline()
        s = answer.split(';')
        return s

    def read_c(self,freq):
        time.sleep(0.5)
        freq=str(freq)       
        self.cnt.write("FREQ "+ freq + ";LEVEL_LOW\n")
        self.cnt.write("MODE_CD;MON_VI\n")
        self.cnt.write("*TRG;C?\n")
        answer = self.cnt.readline()
        try:
            s = answer[:-2].split(' ')
            return float(s[1])
        except:
            return "ERROR"
        
class Gnuplot:
	def __init__(self):
		print "Opening new gnuplot session..."
		self.session = os.popen("gnuplot","w")
	def __del__(self):
		print "Closing gnuplot session..."
		self.session.close()
	def send(self, cmd):
		self.session.write(cmd + '\n')
		self.session.flush()



if __name__ == "__main__":

    rlc = RLC()
    for n in range(5):
##        print time.strftime('%X '),rlc.read_c(100)
        print rlc.read_c(100)

if __name__=="__main__":
	print "Single-window output:"
	g = Gnuplot()
	g.send(RLC)
##	g.send("replot cos(x)")
##	raw_input("press ENTER to continue")
	del g
##
##	print "Multiple window output:"
##	g1 = Gnuplot()
##	g2 = Gnuplot()
##	g1.send("plot sin(x)")
##	g2.send("plot cos(x)")
##	raw_input("press ENTER to continue")
##	del g1
##	del g2

	
##    g = Gnuplot.Gnuplot()
##    g.title('My Systems Plot')
##    g.xlabel('Date')
##    g.ylabel('Value')
##    g('set term png')
##    g('set out "output.png"')
##    #proc = open("response","r")
##    #databuff = Gnuplot.Data(proc.read(), title="test")
##    
##    databuff = Gnuplot.File("response", using='1:2',with_='line', title="test")
##    g.plot(databuff)
       
