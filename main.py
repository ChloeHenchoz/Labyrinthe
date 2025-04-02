"projet labyrinthe 26.03.2025, Natasha et Chloé"
from maprincess import *
from microbit import *

#constantes
WHITE = 0
BLACK = 1
speed = 30

print("depart")
#def calibration():
   # time = time-time()
   
def checkdroite():
    V = False
    droite()
    sleep(1800)
    motor_stop()
    print("droit")
    if (line_sensor(LineSensor.R1)== WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE):
        V = True
    
    gauche()
    sleep(800)
    motor_stop()
    print("check fini ")
    return True 
    
def checkgauche():
    V = False
    gauche()
    sleep(1900)
    motor_stop()
    print("gauche")
    if (line_sensor(LineSensor.R1)== WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE):
        V = True
    
    droite()
    sleep(800)
    motor_stop()
    print("check fini ")
    return True 
    

def toutdroit():
    motor_run(Motor.LEFT, speed, Direction.FORWARD)
    motor_run(Motor.RIGHT, speed, Direction.FORWARD)
    
    

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
        
print(checkdroite())
sleep (1000)
print(checkgauche())
    
    




