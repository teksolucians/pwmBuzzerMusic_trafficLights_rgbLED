import RPi.GPIO as GPIO
import time


btn1 = 11
buzz = 12
btn2 = 13


song = 0

frequency = 1

#notes

#1st Octave
C= 261.63
Csharp=  277.18
D= 293.66
Dsharp = 311.13
E= 329.63
F= 349.23
Fsharp=369.99
G= 392.00
Gsharp= 415.30
A= 440.00
Asharp= 466.16
B= 493.88

#2nd Octave
C2 = 523.25
C2sharp = 554.37
D2 = 587.33
D2sharp = 622.25
E2 = 659.26
F2 = 698.46
F2sharp = 739.99
G2 = 783.99
G2sharp = 830.61
A2 = 880
A2sharp = 932.33
B2 = 987.77
C3 = 1050.25


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(buzz, GPIO.OUT)
    

    
def destroy():
    GPIO.cleanup()
    print("destroy has ran")


    
    
def stop(stop):
        destroy()
        
def loop(): 
    pass

def Mario():
    
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.15)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(E2)
    p.ChangeDutyCycle(1)			
    time.sleep(.15)
    p.ChangeDutyCycle(0)
    time.sleep(.23)
    p.ChangeFrequency(E2)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.01)
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(G2)			
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.5)
    p.ChangeFrequency(G)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.5)
    
    
    p.ChangeFrequency(C2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeFrequency(G)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeFrequency(E)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.4)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(B)		
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(Asharp)			
    p.ChangeDutyCycle(1)
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(A)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    
    
    p.ChangeFrequency(G)		
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(E2)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(G2)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(A2)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(F2)		
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(G2)			
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.27)
    p.ChangeDutyCycle(0)
    time.sleep(.18)
    p.ChangeFrequency(C2)		
    p.ChangeDutyCycle(1)
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.07)
    p.ChangeFrequency(D2)			
    p.ChangeDutyCycle(1)
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.07)
    p.ChangeFrequency(B)		
    p.ChangeDutyCycle(1)
    time.sleep(.25)
    
    p.ChangeDutyCycle(0)    
    time.sleep(.5)
    
    p.ChangeFrequency(C2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeFrequency(G)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeFrequency(E)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.4)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(B)		
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(Asharp)			
    p.ChangeDutyCycle(1)
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(A)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    
    
    p.ChangeFrequency(G)		
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(E2)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(G2)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(A2)
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(F2)		
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(G2)			
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.27)
    p.ChangeDutyCycle(0)
    time.sleep(.18)
    p.ChangeFrequency(C2)		
    p.ChangeDutyCycle(1)
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.07)
    p.ChangeFrequency(D2)			
    p.ChangeDutyCycle(1)
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.07)
    p.ChangeFrequency(B)		
    p.ChangeDutyCycle(1)
    time.sleep(.25)
    
    p.ChangeDutyCycle(0)
    time.sleep(1)
    
    


def Sparrow():
    p.ChangeFrequency(A)		
    p.ChangeDutyCycle(1)
    time.sleep(.25)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)			
    time.sleep(.25)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)			
    time.sleep(.25)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)			
    time.sleep(.25)
    p.ChangeDutyCycle(0)
    time.sleep(.01)
    p.ChangeFrequency(A)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(Fsharp)			
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(G2sharp)
    p.ChangeDutyCycle(1)			
    time.sleep(.7)
    p.ChangeDutyCycle(0)
    time.sleep(1)
    
    
    p.ChangeFrequency(A)			#oth	
    p.ChangeDutyCycle(1)
    time.sleep(.15)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(E2)			#ther
    p.ChangeDutyCycle(1)			
    time.sleep(.15)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(G2sharp)   #wise
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.04)
    p.ChangeFrequency(A)		#late
    p.ChangeDutyCycle(1)			
    time.sleep(.15)
    p.ChangeDutyCycle(0)
    time.sleep(.01)
    p.ChangeFrequency(E2)		#ter
    p.ChangeDutyCycle(1)
    time.sleep(.15)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(G2sharp)		#on	
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.15)
    p.ChangeFrequency(E2)			#in		
    p.ChangeDutyCycle(1)
    time.sleep(.15)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(G2sharp)		#life
    p.ChangeDutyCycle(1)			
    time.sleep(.28)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeFrequency(A)			#you
    p.ChangeDutyCycle(1)			
    time.sleep(.11)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(A)			#go
    p.ChangeDutyCycle(1)			
    time.sleep(.11)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(A)			#catch
    p.ChangeDutyCycle(1)			
    time.sleep(.12)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(G2sharp)		#real
    p.ChangeDutyCycle(1)			
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeFrequency(F2sharp)		#hell
    p.ChangeDutyCycle(1)			
    time.sleep(1.3)
    p.ChangeDutyCycle(0)
    time.sleep(2)
    
    
    
    



def FurElise():
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(D2sharp)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(E2)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(D2sharp)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(B)			
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(D2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.5)
    
    
    p.ChangeFrequency(C)			
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeFrequency(E)		
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)			
    time.sleep(.4)
    p.ChangeFrequency(B)
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeDutyCycle(0)
    time.sleep(.5)

   
    p.ChangeFrequency(E)			
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(Gsharp)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(B)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.5)

    p.ChangeFrequency(E)
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(D2sharp)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(E2)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(D2sharp)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(E2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(B)			
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(D2)		
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)			
    time.sleep(.3)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.5)
    
    
    p.ChangeFrequency(C)			
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeFrequency(E)		
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)			
    time.sleep(.4)
    p.ChangeFrequency(B)
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeDutyCycle(0)
    time.sleep(.5)

    p.ChangeFrequency(E)
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(C2)
    time.sleep(.3)
    p.ChangeFrequency(B)
    time.sleep(.3)
    p.ChangeFrequency(A)
    time.sleep(.6)
    p.ChangeDutyCycle(0)
    time.sleep(2)
    


def Liberty():
    global p
    
    p.ChangeFrequency(Csharp)		#forged
    p.ChangeDutyCycle(1)
    time.sleep(.5)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeDutyCycle(1)			#from
    time.sleep(.5)
    p.ChangeDutyCycle(0)
    time.sleep(.05)
    p.ChangeDutyCycle(1)			#the
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.05)
    p.ChangeDutyCycle(1)			#love
    time.sleep(.7)
    p.ChangeDutyCycle(0)
    time.sleep(.05)
    p.ChangeFrequency(Dsharp)		#of
    p.ChangeDutyCycle(1)
    time.sleep(.70)
    p.ChangeDutyCycle(0)
    p.ChangeFrequency(E)			#li
    p.ChangeDutyCycle(1)
    time.sleep(.85)
    p.ChangeDutyCycle(0)
    time.sleep(.10)
    p.ChangeFrequency(Dsharp)		#ber
    p.ChangeDutyCycle(1)
    time.sleep(.14)
    p.ChangeDutyCycle(0)
    time.sleep(.10)
    p.ChangeFrequency(Csharp)
    p.ChangeDutyCycle(1)			#ty
    time.sleep(.85)
    p.ChangeDutyCycle(0)
    time.sleep(.09)
    ##################################
    p.ChangeFrequency(Csharp)
    p.ChangeDutyCycle(1)
    time.sleep(.45)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(E)
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(Gsharp)
    p.ChangeDutyCycle(1)
    time.sleep(.45)
    p.ChangeDutyCycle(0)
    time.sleep(.075)
    p.ChangeDutyCycle(1)
    time.sleep(.5)
    p.ChangeDutyCycle(0)
    time.sleep(.003)
    p.ChangeFrequency(A)
    p.ChangeDutyCycle(1)
    time.sleep(.75)
    p.ChangeDutyCycle(0)
    time.sleep(.03)
    p.ChangeFrequency(Fsharp)
    p.ChangeDutyCycle(1)
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.15)
    p.ChangeFrequency(Gsharp)
    p.ChangeDutyCycle(1)
    time.sleep(.9)
    p.ChangeDutyCycle(0)
    time.sleep(.75)    
    ######################
    p.ChangeDutyCycle(1)
    time.sleep(.5)
    p.ChangeFrequency(A)
    time.sleep(.5)
    p.ChangeFrequency(Gsharp)
    time.sleep(.5)
    p.ChangeFrequency(Fsharp)
    time.sleep(.5)
    p.ChangeFrequency(E)
    time.sleep(.5)
    p.ChangeFrequency(Dsharp)
    time.sleep(.5)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeFrequency(E)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeDutyCycle(1)
    p.ChangeFrequency(A)
    time.sleep(.65)
    p.ChangeFrequency(Gsharp)
    time.sleep(.25)
    p.ChangeDutyCycle(0)
    time.sleep(.35)
    p.ChangeDutyCycle(1)
    p.ChangeFrequency(Csharp)
    time.sleep(.3)
    p.ChangeFrequency(Dsharp)
    time.sleep(.4)
    p.ChangeDutyCycle(0)
    time.sleep(.05)
    p.ChangeDutyCycle(1)
    p.ChangeFrequency(E)
    time.sleep(.4)
    p.ChangeFrequency(Dsharp)
    time.sleep(1)
    p.ChangeDutyCycle(0)
    time.sleep(2)
    
    
def liberty2():
    p.ChangeFrequency(490)
    p.ChangeDutyCycle(1)
    time.sleep(.6)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(580)
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(680)
    p.ChangeDutyCycle(1)
    time.sleep(.45)
    p.ChangeDutyCycle(0)
    time.sleep(.075)
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeDutyCycle(0)
    time.sleep(.003)
    p.ChangeFrequency(725)
    p.ChangeDutyCycle(1)
    time.sleep(.75)
    p.ChangeDutyCycle(0)
    time.sleep(.03)
    p.ChangeFrequency(650)
    p.ChangeDutyCycle(1)
    time.sleep(.1)
    p.ChangeDutyCycle(0)
    time.sleep(.15)
    p.ChangeFrequency(680)
    p.ChangeDutyCycle(1)
    time.sleep(.9)
    p.ChangeDutyCycle(0)
    time.sleep(5)

def liberty1():  #Forged From the Love of Liberty!
    global p
    
    p.ChangeFrequency(Csharp)		
    p.ChangeDutyCycle(1)
    time.sleep(.6)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeDutyCycle(1)			
    time.sleep(.6)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeDutyCycle(1)			
    time.sleep(.10)
    p.ChangeDutyCycle(0)
    time.sleep(.05)
    p.ChangeDutyCycle(1)			
    time.sleep(.75)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(Dsharp)
    p.ChangeDutyCycle(1)
    time.sleep(.75)
    p.ChangeDutyCycle(0)
    p.ChangeFrequency(E)
    p.ChangeDutyCycle(1)
    time.sleep(1)
    p.ChangeDutyCycle(0)
    time.sleep(.15)
    p.ChangeFrequency(Dsharp)
    p.ChangeDutyCycle(1)
    time.sleep(.19)
    p.ChangeDutyCycle(0)
    time.sleep(.15)
    p.ChangeFrequency(Csharp)
    p.ChangeDutyCycle(1)
    time.sleep(1)
    p.ChangeDutyCycle(0)
    time.sleep(2.5)
    
    
def Tempa():
    
    p.ChangeFrequency(G2) #T
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.025)
    p.ChangeFrequency(Fsharp)  #E
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.001)
    p.ChangeFrequency(C2sharp)  #M
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.05)
    p.ChangeFrequency(Fsharp)  #P
    p.ChangeDutyCycle(1)
    time.sleep(.18)
    p.ChangeDutyCycle(0)
    time.sleep(.06)
    p.ChangeFrequency(D2)  #A
    p.ChangeDutyCycle(1)
    time.sleep(.28)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(F)   #IN
    p.ChangeDutyCycle(1)
    time.sleep(.08)
    p.ChangeDutyCycle(0)
    time.sleep(.05)
    p.ChangeFrequency(G)   #THE
    p.ChangeDutyCycle(1)
    time.sleep(.08)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(E)   #CEN -
    p.ChangeDutyCycle(1)
    time.sleep(.13)
    p.ChangeDutyCycle(0)
    time.sleep(.09)
    p.ChangeFrequency(D)    #TER
    p.ChangeDutyCycle(1)
    time.sleep(.10)
    p.ChangeDutyCycle(0)
    time.sleep(2)
    
def FarmerNappy():
    
    p.ChangeFrequency(B) #IF
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.025)
    p.ChangeFrequency(E2)  #YOU
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.025)
    p.ChangeFrequency(G2)  #WANT
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.05)
    p.ChangeFrequency(A2)  #ME
    p.ChangeDutyCycle(1)
    time.sleep(.7)
    p.ChangeDutyCycle(0)
    time.sleep(.07)
    p.ChangeFrequency(G2)  #TO
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.01)
    p.ChangeFrequency(E2)   #GO
    p.ChangeDutyCycle(1)
    time.sleep(.9)
    p.ChangeFrequency(D2)   #O-OH
    p.ChangeDutyCycle(1)
    time.sleep(1)
    p.ChangeDutyCycle(0)
    time.sleep(.25)
    p.ChangeDutyCycle(1)	 #you
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeDutyCycle(1)     #Can't
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeDutyCycle(1)     #Be
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)	#look
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(D2)	#ing
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)	#the
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(D2)	#way
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(C2)	#you
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(A)	#do
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(G)	#do-oo
    p.ChangeDutyCycle(1)
    time.sleep(.5)
    p.ChangeDutyCycle(0)
    time.sleep(.5)
    
    p.ChangeFrequency(D2)
    p.ChangeDutyCycle(1)	 #you
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeDutyCycle(1)     #Can't
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeDutyCycle(1)     #Be
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)	#cook
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(D2)	#ing
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)	#the
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(D2)	#way
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(C2)	#you
    p.ChangeDutyCycle(1)
    time.sleep(.3)
    p.ChangeDutyCycle(0)
    time.sleep(.1)
    p.ChangeFrequency(A)	#do
    p.ChangeDutyCycle(1)
    time.sleep(.4)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(G)	#do-oo
    p.ChangeDutyCycle(1)
    time.sleep(.5)
    p.ChangeDutyCycle(0)
    time.sleep(.5)
    
    
    
    p.ChangeFrequency(D2)
    p.ChangeDutyCycle(1)	 #you
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeDutyCycle(1)     #Can't
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeDutyCycle(1)     #Be
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(C2)
    p.ChangeDutyCycle(1)	#hook
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.02)
    p.ChangeFrequency(D2)	#ing
    p.ChangeDutyCycle(1)
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(.2)
    p.ChangeFrequency(D2)
    p.ChangeDutyCycle(1)	#me
    time.sleep(.2)
    p.ChangeDutyCycle(0)
    time.sleep(2)
    
    
    
    
def jukebox(tune):
   
 
   global song
   song = (song + 1)%6
   print(song)
   if song==0:
       Liberty()
   if song==1:
        Mario()
   if song==2:
       FarmerNappy()
   if song==3:
       FurElise()
   if song==4:
       Tempa()
   if song==5:
       Sparrow()
       
    
    
if __name__=='__main__':
    
    setup()
    p = GPIO.PWM(buzz, frequency)
    p.start(0)
   
    GPIO.add_event_detect(btn1, GPIO.FALLING, callback=jukebox,bouncetime=200)
    GPIO.add_event_detect(btn2, GPIO.FALLING, callback=stop,bouncetime=200)
    while True:
        try:
            pass
        except KeyboardInterrupt:
            destroy()