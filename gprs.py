import serial
import time
from curses import ascii
import serial.tools.list_ports
import sys
import threading

phone = serial.Serial("/dev/ttyUSB3", baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=0.01, rtscts=True, dsrdtr=True)

option = -1

raspuns = ""
raspuns_nou = ""

def Citire_comanda():
    
    counter = 0
    mesaj_citit = 0
    comanda = ""
    
    phone.write(str.encode('at+cgsockcont=1,"IP","live.vodafone.com"\r\n'))
    time.sleep(0.2)
    phone.write(str.encode('at+csocksetpn=1\r\n'))
    time.sleep(0.2)
    
    phone.write(str.encode('at+cipmode=0\r\n'))
    time.sleep(0.2)
    phone.write(str.encode('at+netopen\r\n'))
    time.sleep(0.2)
    phone.write(str.encode('at+cipopen=0,"TCP","172.104.230.27",12345\r\n'))
    time.sleep(0.3)
  
    phone.write(str.encode('at+cipsend=0,21\r\n'))
    time.sleep(0.5)

    phone.write(str.encode('Robot:Request Command\r\n'))
    
    while counter < 60 and mesaj_citit != 1:
        
        try:
    
            line = phone.read(400).decode('ascii').strip()
            #print("abcd")
            if line:
                #print(line)
                index_start = line.find("Comanda:")
                index_end = line.find(';')
                
                if index_start != -1 and index_end != -1:
                    comanda = line[index_start+8:index_end]
                    mesaj_citit = 1

            counter = counter + 1
        except:
            pass
    
        
    time.sleep(0.7)
    
    return comanda

def Control_GPRS():
    
    global raspuns
    global raspuns_nou
    
    while True:
        raspuns = Citire_comanda()
        if raspuns:
            print(raspuns)
            raspuns_nou = raspuns
        else:
            print("Nu s-a primit niciun mesaj nou")

        
def thread_testing():

    while True:
        print("thread 2")
        time.sleep(0.5)


if __name__=="__main__":
    
    while (option!=0):
        
        print("------------------------------\nOptions:\n0) Exit\n1) Citire comanda\n")
        option = int(input("Enter your option here:"))
        
        if (option == 0):
            break
        elif (option == 1):
            t1 = threading.Thread(target = Control_GPRS)
            
            t1.start()

            while True:
                print("Procesul principal foloseste comanda: " + raspuns_nou)
                time.sleep(0.5)
            
            t1.join()

            
        else:
            print("Optiune nevalida\n");
            


