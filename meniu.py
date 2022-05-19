import serial
import time
from curses import ascii
import serial.tools.list_ports
import sys

phone = serial.Serial("/dev/ttyUSB2", baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=0.01, rtscts=True, dsrdtr=True)

option = -1

raspuns = ""

def trimitere_mesaj():
    
    print("Cui doriti sa ii trimiteti un mesaj?")
    numar_telefon = input()
    print("Ce mesaj doriti sa trimiteti?")
    mesaj = input()

    phone.write(str.encode('at+cmgs="'+numar_telefon+'"\r\n'))
    phone.write(str.encode(mesaj))
    phone.write(str.encode(ascii.ctrl('z')))

     
def citire_ultim_mesaj():
    
    counter = 0
    mesaj_citit = 0
    comanda = ""
    
    phone.write(str.encode('at\r\n'))
    phone.write(str.encode('at+cmgf=1\r\n'))                       
    phone.write(str.encode('at+cmgr=0\r\n'))
    
    while counter < 3 and mesaj_citit != 1:
        
        #try:
            
        line = phone.read(200).decode('ascii').strip()
        if line:
            #print(line)
            index_start = line.find("Comanda:")
            index_end = line.find(';')
            
            if index_start != -1 and index_end != -1:
                file_object = open("log_mesaje.txt","a")
                comanda = line[index_start+8:index_end]
                file_object.write(line[index_start+8:index_end]+'\n')
                file_object.close()
                mesaj_citit = 1
        #except:
            #pass
        
        counter = counter + 1

    phone.flush()
    phone.write(str.encode('at+cmgd=0,4\r\n'))
    
    time.sleep(0.5)
    return comanda
    
    
def at_command():
    
    phone.write(str.encode('at\r\n'))
        
    try:
        line = phone.read(100).decode('ascii')#.strip()
        if line:
            print(line)
    except:
        pass
    
    phone.flush()
        
if __name__=="__main__":
    
    while (option!=0):
        
        print("------------------------------\nOptions:\n0) Exit\n1) Trimite mesaj\n2) Citeste ultimul mesaj\n3) AT command")
        option = int(input("Enter your option here:"))
        
        if (option == 0):
            break
        elif (option == 1):
            trimitere_mesaj()
        elif (option == 2):
            raspuns = citire_ultim_mesaj()
            if raspuns:
                print(raspuns)
            else:
                print("Nu s-a primit niciun mesaj nou")
        elif (option == 3):
            at_command()
        else:
            print("Optiune nevalida\n");
            
            
