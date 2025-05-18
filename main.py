"""Projet Laby 18.05.25 """

#Imports

from maprincess import *
from microbit import *
import radio
        
    
#Constantes

WHITE = 0
BLACK = 1
speed = 13


#Définitions

def Tout_Droit(): # Tant que R2 + R1 sont sur la ligne et que M n'y est pas, on avance jusqu'à que M arrive sur une ligne (j'ai enlevé la condition pour L1 qui contribuait au bug je crois) 
    
    if (line_sensor(LineSensor.M) == WHITE and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK )  :
        
        led_rgb(Color.WHITE)
        
        
        while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==BLACK):
            motor_run(Motor.ALL, speed +10, Direction.FORWARD)
            sleep(40)
        
        
 
       
        
        
        while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==WHITE and line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.L1)==WHITE):
            led_rgb(Color.ORANGE)
            motor_run(Motor.LEFT, speed, Direction.FORWARD)
            motor_run(Motor.RIGHT, speed +20 , Direction.FORWARD)
            sleep(25)
            
        
        
#     if (line_sensor(LineSensor.R1)== BLACK and line_sensor(LineSensor.R2)==WHITE ):
#         motor_run(Motor.LEFT, speed, Direction.FORWARD)
#         motor_run(Motor.RIGHT, speed , Direction.FORWARD)
       
#         sleep(100)
#         while (line_sensor_all() == (1, 1, 0, 1, 0) or line_sensor_all() == (0, 0, 1, 1, 1)):
#             led_rgb(Color.RED)
#             motor_run(Motor.LEFT, speed +10 , Direction.BACKWARD)
#             motor_run(Motor.RIGHT, speed -5 , Direction.BACKWARD)
#             sleep(25)
      
            
    
def Coin(): # si M + R1 + R2 sont sur une ligne, ce qui devrait être un coin, on tourne sur place jusqu'à que M ne soit plus sur la ligne
    Fini()
    
    if (line_sensor(LineSensor.M) == BLACK and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK):
        led_rgb(Color.BLUE)
         
        while not line_sensor(LineSensor.M) == WHITE:
      
            motor_run(Motor.LEFT, speed + 10, Direction.BACKWARD)
            motor_run(Motor.RIGHT, speed + 10, Direction.FORWARD)
            sleep(25)
        
        

       
 
 
        
        if (line_sensor_all() == (0, 1, 0, 0, 0) or line_sensor_all() == (1, 1, 0, 0, 0) or line_sensor_all() == (0, 1, 0, 1, 1)): #  dans les deux config qui font que le robot s'arrête completement, on le fait reculer un peu pour qu'il reparte ( imite un coup de pouce) 
           motor_run(Motor.ALL, speed, Direction.BACKWARD)
           sleep(100)
       
   
        

        
        if (line_sensor(LineSensor.M) == BLACK and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK and line_sensor(LineSensor.L1) == BLACK ):
            
            led_rgb(Color.VIOLET)
            motor_run(Motor.LEFT, speed, Direction.BACKWARD)
            sleep(1000)
            motor_stop()
            motor_run(Motor.RIGHT, speed, Direction.BACKWARD)
            sleep(1000)
            
         
           
        while (line_sensor_all() == (1, 1, 0, 1, 0)) :
            Fini()
            led_rgb(Color.VIOLET)
            motor_run(Motor.ALL, speed, Direction.BACKWARD)
            sleep(25)
        
  
            
def Edge():  # si on rencontre un bord, c'est à dire que M et R1 ne sont plus sur la ligne mais R2 si, on tourne à droite pour en "faire le tour" jusqu'à que R2 +R1 soient sur la ligne mais pas M 
    Fini()
    if (line_sensor(LineSensor.M) == WHITE and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == WHITE):
        led_rgb(Color.GREEN)
#         motor_stop()
        sleep(350)
        
#         led_rgb(Color.RED)
#         motor_run(Motor.RIGHT, speed +10, Direction.FORWARD)
#         motor_run(Motor.LEFT, speed + 10 , Direction.FORWARD)
#         sleep(500)
#             
        
        while not line_sensor(LineSensor.R1) == BLACK:
            Fini()
            led_rgb(Color.VIOLET)
            motor_run(Motor.RIGHT, 0 , Direction.FORWARD)
            motor_run(Motor.LEFT, speed +15 , Direction.FORWARD)
            sleep(50)
            
        if line_sensor(LineSensor.R2) == WHITE:
            while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==WHITE and line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.L1)==WHITE):
                Fini()
                led_rgb(Color.PURPLE)
                motor_run(Motor.LEFT, speed, Direction.FORWARD)
                motor_run(Motor.RIGHT, speed +20 , Direction.FORWARD)
                sleep(25)
                
            
            sleep(50)
#         if (line_sensor(LineSensor.R1) == BLACK and line_sensor(LineSensor.R2) == WHITE):
#             while not line_sensor(LineSensor.R2) == BLACK:
#                 motor_run(Motor.RIGHT, speed , Direction.BACKWARD)
#                 motor_run(Motor.LEFT, speed , Direction.BACKWARD)
#                 sleep(25)
#             motor_stop()
#             sleep(10)
#             motor_run(Motor.RIGHT, speed + 10, Direction.FORWARD)
#             motor_run(Motor.LEFT, speed + 10 , Direction.BACKWARD)
#             sleep(100)
#             
            
            
      
        
        
#      
#         while not (line_sensor(LineSensor.M) == WHITE and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK ):
#             while not line_sensor(LineSensor.R1) == BLACK:
#                 motor_run(Motor.RIGHT, 0 , Direction.FORWARD)
#                 motor_run(Motor.LEFT, speed + 10 , Direction.FORWARD)
#                 sleep(10)
#                 print( "1")
#             while line_sensor(LineSensor.R2) == WHITE:
#                 motor_run(Motor.RIGHT, speed , Direction.FORWARD)
#                 motor_run(Motor.LEFT, speed  , Direction.FORWARD)
#                 sleep(15)
#                 print( "2")
#             print("3")
#             
#            
 
            
         
def Fini():
    x = ultrasonic()
    print(x)
    if 3 < x < 6 :
        Run = False
         
                
        
            

        

# Boucle principale

Run = True

while True :
    while Run == True:
    

    

        Tout_Droit()
        sleep(25)
        
        Coin()
        sleep(25)
        
        Edge()
        sleep(25)
        
       
        sleep(25)
        
    motor_stop()
    
        
    
    


