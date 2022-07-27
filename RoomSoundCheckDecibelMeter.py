#!/usr/bin/python

import sys
import usb.core
import requests
import time
import pygame
import math

pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Music/Achmed the dead terrorist - Silence, I kill You.mp3")

dev=usb.core.find(idVendor=0x16c0,idProduct=0x5dc)

def akou():
    time.sleep(1)
    ret = dev.ctrl_transfer(0xC0,4,0,0,200)
    dB = (ret[0]+((ret[1]&3)*256))*0.1+30
    return dB
        
while True:
    dB = akou()
    
    i=0
    
    if dB > 60:
        print("I track a sound over 60 dB")
        while True:
            dB = akou()
            print(dB)
            minutelist =[]
            sumofsound = 0.0
            apolititimi = 0
            #print(i) isws na mhn xreiazetai na einai edw to while giati xanw 1 sec / enan elegxo

            while i < 10:
                dB = akou()
                                
                minutelist.append(dB)
                print("The list of the sounds is track:",minutelist)
                i=i+1
                print("Check No",i)
                
                list_lengeth = len(minutelist)
                sumofsound = math.fsum(minutelist)
                print("The total sum of the sounds is",sumofsound, "dB")
                apolititimi = sumofsound/i
                print("The average sound for this period of time is",apolititimi,"dB")
                
                
                if apolititimi > 50 and i == 10:
                    print("Silence pleace, the room is too noisy")
                    pygame.mixer.music.play()
                    time.sleep(10)
                elif apolititimi <= 50 and i == 10:
                    print("I am happy, the noice was instant")
                    
                    break
                    
            else:
                print("Lets start checking the sounds again")
                
                break

    else:
        print ("Silence in the room, only ", dB,"dB")
        #i=0 #isws na mhn xreiazetai giati yparxei sthn arxi prin to while
        

