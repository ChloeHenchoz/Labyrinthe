"projet labyrinthe 26.03.2025, Natasha et Chloé"
from maprincess import *
from microbit import *

#constantes
WHITE = 0
BLACK = 1
speed = 30

print("depart")
led_rgb(Color.WHITE)
#def calibration():
   # time = time-time()
   
def checkdroite():
    led_rgb(Color.RED)# renvoit true si y'a pas de mur 
    V = False
    droite()
    sleep(1800)
    motor_stop()
    print("droit")
    if (line_sensor(LineSensor.R1)== WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE):
        V = True
    
    while not (line_sensor(LineSensor.R1)== BLACK and line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.M)==BLACK):
        gauche()
    motor_stop()
    
    sleep(100)
    print("check fini ")
    
    return (V)
    
def checkgauche():
    led_rgb(Color.BLUE)# renvoit true si y'a pas de mur 
    V = False
    gauche()
    sleep(900)
    motor_stop()
    print("gauche")
    if (line_sensor(LineSensor.R1)== WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE):
        V = True
    
    #while not line_sensor(LineSensor.R1)== BLACK:
     #   droite()
    
    #motor_stop()
    #print("check fini ")
    sleep(500)
    return (V)
    

def decision ():
    mur_gauche = checkgauche()
    mur_droite = checkdroite()
    led_rgb(Color.WHITE)
    if (mur_gauche == True  and mur_droite == False) :
        gauche()
        sleep(900)
        motor_stop()
    elif mur_droite == True  :
        droite()
        sleep(900)
        motor_stop()
    elif (mur_gauche == True  and mur_droite == True):
        gauche()
        sleep(1800)
    
        motor_stop()
     #   mur_droite = checkdroite()
    #if (mur_droite == True and mur_gauche == False):
     #   droite()
      #  sleep(1200)
     #   motor_stop()
    #elif (mur_droite == False and mur_gauche == False):
     #   toutdroit()
    #motor_stop()
    #sleep(800)
   # toutdroit()
    
        
def toutdroit():
    while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==BLACK):
        
    #while not (line_sensor(LineSensor.R1)== BLACK and line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.M)==BLACK):
        motor_run(Motor.LEFT, speed, Direction.FORWARD)
        motor_run(Motor.RIGHT, speed, Direction.FORWARD)
        
        sleep(120)
    motor_stop()

def droite():
    
    motor_run(Motor.LEFT, speed, Direction.FORWARD)
    motor_run(Motor.RIGHT, speed, Direction.BACKWARD)
    
def gauche():
    while line_sensor(LineSensor.L1)== BLACK:
        motor_run(Motor.LEFT, speed, Direction.BACKWARD)
        motor_run(Motor.RIGHT, speed, Direction.FORWARD)
    
#while True :
    
    ##sleep(100)
   #print("boucle")
   # if (line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE) :
    #    toutdroit()
    #    print("je roule")
        
    #if (line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.M)==BLACK) :
    #    while not (line_sensor(LineSensor.R1)== WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE):
      #      droite()
            
            
        #motor_stop()
        #print("je m'arrête")
        #sleep(200)
        #droite()
        #sleep(1000)
        #motor_stop()
        #toutdroit()
def resteblanc ():
    if line_sensor(LineSensor.R2)== BLACK:
        while not line_sensor(LineSensor.R2)== WHITE:
            led_rgb(Color.RED)
            motor_run(Motor.LEFT, speed, Direction.FORWARD)
            motor_run(Motor.RIGHT, speed-10 , Direction.FORWARD)
            sleep(100)
            motor_stop()
            sleep(100)
    if line_sensor(LineSensor.L2)== BLACK:    
        while not line_sensor(LineSensor.L2)== WHITE:
            led_rgb(Color.BLUE)
            motor_run(Motor.LEFT, speed -10 , Direction.FORWARD)
            motor_run(Motor.RIGHT, speed , Direction.FORWARD)
            sleep(100)
            motor_stop()
            sleep(100)
    
    
    

while True:
    led_rgb(Color.WHITE)
    toutdroit()
    #gauche()
   # resteblanc()
    #decision()


 

    






