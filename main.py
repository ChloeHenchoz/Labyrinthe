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
   
def checkdroite():  # renvoit true si y'a pas de mur 
    V = False
    droite()
    sleep(1200)
    motor_stop()
    print("droit")
    if (line_sensor(LineSensor.R1)== WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE):
        V = True
    
    gauche()
    sleep(800)
    motor_stop()
    print("check fini ")
    sleep(500)
    return (V)
    
def checkgauche(): # renvoit true si y'a pas de mur 
    V = False
    gauche()
    sleep(1000)
    motor_stop()
    print("gauche")
    if (line_sensor(LineSensor.R1)== WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE):
        V = True
    
    while not line_sensor(LineSensor.R1)== BLACK:
        droite()
    
    motor_stop()
    print("check fini ")
    sleep(500)
    return (V)
    

def decision ():
    mur_gauche = checkgauche()
    
    if mur_gauche == True  :
        #gauche()
        sleep(1100)
        motor_stop()
    #else:
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
    while not (line_sensor(LineSensor.R1)== BLACK and line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.M)==BLACK):
        motor_run(Motor.LEFT, speed, Direction.FORWARD)
        motor_run(Motor.RIGHT, speed, Direction.FORWARD)
        
        sleep(50)
    motor_stop()

def droite():
    motor_run(Motor.LEFT, speed, Direction.FORWARD)
    motor_run(Motor.RIGHT, speed, Direction.BACKWARD)
    
def gauche():
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


while True:
    toutdroit()
    decision()


 

    




