

import Adafruit_ADS1x15
import serial
import time
import requests

rate = [0]*10
amp = 100
GAIN = 2/3  
curState = 0
stateChanged = 0

ser = serial.Serial ("/dev/ttyS0", 9600)


def send_to_prcessing(data):     #for Heart rate Sensor
        ser.write(str(data).encode())
       
def sms_send():
    url="https://www.fast2sms.com/dev/bulk"
    params={
  
        "authorization":"fvaKUPuNimZCWE8MOpB9YjLGs4nyeg6lzRqS71JXH5QFw3cktDIm3puGNrOFLP2Bq0AzjDfsWtVCTe6x",
        "sender_id":"SMSINI",
        "message":"Heart rate High",
        "language":"english",
        "route":"p",
        "numbers":"9607181257"
    }
    rs=requests.get(url,params=params)

def read_pulse():
    firstBeat = True
    secondBeat = False
    sampleCounter = 0
    lastBeatTime = 0
    lastTime = int(time.time()*1000)
    th = 525
    P = 512
    T = 512
    IBI = 600
    Pulse = False
    adc = Adafruit_ADS1x15.ADS1115()
    i=1
    while i==1:
        Signal = adc.read_adc(0, gain=GAIN)   
        curTime = int(time.time()*1000)
        send_to_prcessing(Signal)
        sampleCounter += curTime - lastTime
        lastTime = curTime
        N = sampleCounter - lastBeatTime

        if Signal > th and  Signal > P:          
            P = Signal
     
        if Signal < th and N > (IBI/5.0)*3.0 :  
            if Signal < T :                      
              T = Signal                                                 
        
        if N > 250 :                              
            if  (Signal > th) and  (Pulse == False) and  (N > (IBI/5.0)*3.0)  :       
              Pulse = 1;                       
              IBI = sampleCounter - lastBeatTime
              lastBeatTime = sampleCounter       

              if secondBeat :                     
                secondBeat = 0;               
                for i in range(0,10):             
                  rate[i] = IBI                      

              if firstBeat :                        
                firstBeat = 0                  
                secondBeat = 1                  
                continue                              

              runningTotal = 0;               
              for i in range(0,9):            
                rate[i] = rate[i+1]       
                runningTotal += rate[i]      

              rate[9] = IBI;                  
              runningTotal += rate[9]        
              runningTotal /= 10;             
              BPM = 60000/runningTotal       
              print("BPM:" + str(BPM))
              send_to_prcessing(BPM)
              send_to_prcessing(IBI)
              sms_send()
             

        if Signal < th and Pulse == 1 :                    
            amp = P - T                   
            th = amp/2 + T
            T = th
            P = th
            Pulse = 0 
            

        if N > 2500 :
            th = 512
            T = th                  
            P = th                                              
            lastBeatTime = sampleCounter
            firstBeat = 0                     
            secondBeat = 0                   
            print("no beats found")
            break

        time.sleep(0.005)

        
while True:                    
      read_pulse() 

