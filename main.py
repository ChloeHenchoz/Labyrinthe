"""Projet Laby 18.05.25"""

#Imports

from maprincess import *
from microbit import *

#Constantes

WHITE = 0
BLACK = 1
speed = 13


#Définitions

def Tout_Droit(): # Tant que R2 + R1 sont sur la ligne et que M n'y est pas, on avance jusqu'à que M arrive sur une ligne  
    
    if (line_sensor(LineSensor.M) == WHITE and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK )  :
        
        led_rgb(Color.WHITE)
        
        
        while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==BLACK):
            motor_run(Motor.ALL, speed +10, Direction.FORWARD)
            sleep(40)
        
       
#       Si on dépasse la ligne en allant trop à droite (R2 ==WHITE), on corrige en allant plus vite d'un côté 
        while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==WHITE and line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.L1)==WHITE):
            led_rgb(Color.ORANGE)
            motor_run(Motor.LEFT, speed, Direction.FORWARD)
            motor_run(Motor.RIGHT, speed +20 , Direction.FORWARD)
            sleep(25)
            
        
        
    
def Coin(): # si M + R1 + R2 sont sur une ligne, ce qui devrait être un coin, on tourne sur place jusqu'à que M ne soit plus sur la ligne
    
    
    if (line_sensor(LineSensor.M) == BLACK and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK):
        led_rgb(Color.BLUE)
         
        while not line_sensor(LineSensor.M) == WHITE:
      
            motor_run(Motor.LEFT, speed + 10, Direction.BACKWARD)
            motor_run(Motor.RIGHT, speed + 10, Direction.FORWARD)
            sleep(25)
        
        
       
            
def Edge():  # si on rencontre un bord, c'est à dire que M et R1 ne sont plus sur la ligne mais R2 si, on tourne à droite pour en "faire le tour" jusqu'à que R2 +R1 soient sur la ligne mais pas M 
    
    if (line_sensor(LineSensor.M) == WHITE and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == WHITE):
        led_rgb(Color.GREEN)

        sleep(350)
        

        
        while not line_sensor(LineSensor.R1) == BLACK: # on tourne tant qu'on a pas atteint la ligne avec R1 
            
            led_rgb(Color.VIOLET)
            motor_run(Motor.RIGHT, 0 , Direction.FORWARD)
            motor_run(Motor.LEFT, speed +15 , Direction.FORWARD)
            sleep(50)
            
        if line_sensor(LineSensor.R2) == WHITE: # Si on est pas bien alligné quand on a fini de tourné, on corrige pour pouvoir continuer (sinon on ne peut entrer dans aucune des autres boucles ) 
            while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==WHITE and line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.L1)==WHITE):
           
                led_rgb(Color.PURPLE)
                motor_run(Motor.LEFT, speed, Direction.FORWARD)
                motor_run(Motor.RIGHT, speed +20 , Direction.FORWARD)
                sleep(25)
                
            
            sleep(50)
            

      
            
         
def Fini():  #  on verifie s'il y a un objet tout proche, pour finir le labyrinthe en sortant de la boucle while fini() == True 
    x = ultrasonic()
    print(x)
    if 3 < x < 6 :
        
        return False
    return True
         
        

# Boucle principale

while True :
    
    while Fini() == True:
    

    

        Tout_Droit()
        sleep(25)
       
        
        Coin()
        sleep(25)
        
        
        Edge()
        sleep(25)
        
        
        sleep(25)
       
        
    motor_stop()
   
    
        
    
    


