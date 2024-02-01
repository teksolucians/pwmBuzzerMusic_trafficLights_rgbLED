import RPi.GPIO as GPIO
import time


#jukebox setup section

btn1 = 11  #play jukebox button
buzz = 7

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





#RGB lED Variable Assignment Section
# RGB LED Pin assignments (adjust according to your setup)
red_pin = 21
green_pin = 13
blue_pin = 15
button_red = 16
button_green = 18
button_blue = 22

# Initial color values
red = 0
green = 0
blue = 0

# Initial color intensities
current_red_intensity = 0
current_green_intensity = 0
current_blue_intensity = 0






#traffic lights Variable Assignment section

btn2 = 12   #traffic lights activation button
north_red = 24
north_yellow = 26
north_green = 32

south_red = 36
south_yellow = 38
south_green = 40







def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(buzz, GPIO.OUT)
    
    #Initialize GPIO
    GPIO.setup(red_pin, GPIO.OUT)
    GPIO.setup(green_pin, GPIO.OUT)
    GPIO.setup(blue_pin, GPIO.OUT)
    GPIO.setup(button_red, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button_blue, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    
   
    
    # Setup for north bound traffic lights
    GPIO.setup(north_red, GPIO.OUT)
    GPIO.setup(north_yellow, GPIO.OUT)
    GPIO.setup(north_green, GPIO.OUT)
    
    # Setup for south bound traffic lights
    GPIO.setup(south_red, GPIO.OUT)
    GPIO.setup(south_yellow, GPIO.OUT)
    GPIO.setup(south_green, GPIO.OUT)
    
    # Initialize all traffic lights to off
    GPIO.output(north_red, GPIO.LOW)
    GPIO.output(north_yellow, GPIO.LOW)
    GPIO.output(north_green, GPIO.LOW)
    GPIO.output(south_red, GPIO.LOW)
    GPIO.output(south_yellow, GPIO.LOW)
    GPIO.output(south_green, GPIO.LOW)
    
    
        
def destroy():
    GPIO.cleanup()
    print("destroy has ran")


    


def traffic_lights(channel):
            while True:
                # North green, South red
                GPIO.output(north_green, GPIO.HIGH)
                GPIO.output(north_yellow, GPIO.LOW)
                GPIO.output(north_red, GPIO.LOW)
                GPIO.output(south_green, GPIO.LOW)
                GPIO.output(south_yellow, GPIO.LOW)
                GPIO.output(south_red, GPIO.HIGH)
                time.sleep(5)  # Green light duration
                
                # North yellow, South red to yellow
                GPIO.output(north_green, GPIO.LOW)
                GPIO.output(north_yellow, GPIO.HIGH)
                time.sleep(2)  # Yellow light duration
                
                # North red, South green
                GPIO.output(north_yellow, GPIO.LOW)
                GPIO.output(north_red, GPIO.HIGH)
                
                GPIO.output(south_yellow, GPIO.LOW)
                time.sleep(1)
                GPIO.output(south_red, GPIO.LOW)
                GPIO.output(south_green, GPIO.HIGH)
                time.sleep(5)  # Green light duration
                
                # South yellow, North stays red
                GPIO.output(south_green, GPIO.LOW)
                GPIO.output(south_yellow, GPIO.HIGH)
                time.sleep(2)  # Yellow light duration
                
                # Reset to start of cycle
                GPIO.output(south_yellow, GPIO.LOW)
                GPIO.output(south_red, GPIO.HIGH)  
                time.sleep(1)
                GPIO.output(north_red,GPIO.LOW)
                GPIO.output(north_green,GPIO.HIGH)


        
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
   print("Song ",song)
   if song==0:
       print("Trinidad National Anthem")
       Liberty()
   if song==1:
        print("Super Mario Theme Song")
        Mario()
   if song==2:
       print("Farmer Nappy")
       FarmerNappy()
   if song==3:
       print("Fur Elise")
       FurElise()
   if song==4:
       print("T E M P A in the soca")
       Tempa()
   if song==5:
       print("Sparrow - Children go to school and learn well")
       Sparrow()
       

def update_led_colors():
    red_pwm.ChangeDutyCycle(current_red_intensity / 255 * 100)
    green_pwm.ChangeDutyCycle(current_green_intensity / 255 * 100)
    blue_pwm.ChangeDutyCycle(current_blue_intensity / 255 * 100)




def red(channel):
    global current_red_intensity
    current_red_intensity = (current_red_intensity + 50) % 256
    update_led_colors()
    print_current_color_values()
    reset_colors_if_all_pressed(channel)

def green(channel):
    global current_green_intensity
    current_green_intensity = (current_green_intensity + 50) % 256
    update_led_colors()
    print_current_color_values()
    reset_colors_if_all_pressed(channel)

def blue(channel):
    global current_blue_intensity
    current_blue_intensity = (current_blue_intensity + 50) % 256
    update_led_colors()
    print_current_color_values()
    reset_colors_if_all_pressed(channel)



def print_current_color_values():
    print("Current Color Intensities:")
    print(f"Red: {current_red_intensity}")
    print(f"Green: {current_green_intensity}")
    print(f"Blue: {current_blue_intensity}")


            
def reset_colors_if_all_pressed(channel):
    # Check the current state of all buttons
    if not GPIO.input(button_red) and not GPIO.input(button_green) and not GPIO.input(button_blue):
        # All buttons are pressed, reset color intensities
        global current_red_intensity, current_green_intensity, current_blue_intensity
        current_red_intensity = 0
        current_green_intensity = 0
        current_blue_intensity = 0
        update_led_colors()
        print("All colors reset to 0.")


                        
            
            
            
if __name__=='__main__':
    
    setup()
    p = GPIO.PWM(buzz, frequency)
    p.start(0)
    
    
    # Create PWM objects for smooth color transitions
    red_pwm = GPIO.PWM(red_pin, 100)  
    green_pwm = GPIO.PWM(green_pin, 100)
    blue_pwm = GPIO.PWM(blue_pin, 100)
    red_pwm.start(0)  # Start PWM with 0 duty cycle
    green_pwm.start(0)
    blue_pwm.start(0)
       
    GPIO.add_event_detect(btn1, GPIO.FALLING, callback=jukebox,bouncetime=500)
    GPIO.add_event_detect(btn2, GPIO.FALLING, callback=traffic_lights,bouncetime=500)
    GPIO.add_event_detect(button_red, GPIO.FALLING, callback=red,bouncetime=500)
    GPIO.add_event_detect(button_green, GPIO.FALLING, callback=green,bouncetime=500)
    GPIO.add_event_detect(button_blue, GPIO.FALLING, callback=blue,bouncetime=500)
    
    
    