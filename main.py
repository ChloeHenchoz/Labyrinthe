"""Projet Laby 04.05.25 """
#Imports

from maprincess import *
from microbit import *

#Constantes

WHITE = 0
BLACK = 1
speed = 20

#Définitions

def Tout_Droit(): # Tant que R2 + R1 sont sur la ligne et que M n'y est pas, on avance jusqu'à que M arrive sur une ligne 
    
    if (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==BLACK  and line_sensor(LineSensor.L1)==WHITE):
        led_rgb(Color.WHITE)
        
        while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.L1)==WHITE):
            motor_run(Motor.ALL, speed, Direction.FORWARD)
            sleep(50)
        
        
        motor_stop()
        print(line_sensor_data_all())
        print(line_sensor_all())
        print("motor stop 1")
        
        
        while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==WHITE and line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.L1)==WHITE):
            led_rgb(Color.ORANGE)
            motor_run(Motor.LEFT, speed, Direction.FORWARD)
            motor_run(Motor.RIGHT, speed +20 , Direction.FORWARD)
            sleep(50)
            
        motor_stop()
        print(line_sensor_data_all())
        print(line_sensor_all())
        print("motor stop 2")
    
def Coin(): # si M + R1 + R2 sont sur une ligne, ce qui devrait être un coin, on tourne sur place jusqu'à que M ne soit plus sur la ligne
    
    if (line_sensor(LineSensor.M) == BLACK and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK):
        led_rgb(Color.BLUE)
         
        while not line_sensor(LineSensor.M) == WHITE:   
            motor_run(Motor.LEFT, speed, Direction.BACKWARD)
            motor_run(Motor.RIGHT, speed, Direction.FORWARD)
            sleep(50)
            
        motor_stop()
        
#         while not ( line_sensor(LineSensor.R1) == BLACK and line_sensor(LineSensor.R2) == BLACK): # si R1 et/ou R2 ne sont plus sur la ligne on cherche à retrouver la ligne en avançant plus vite à gauche 
#             led_rgb(Color.RED)
#             motor_run(Motor.LEFT, speed + 10, Direction.FORWARD)
#             motor_run(Motor.RIGHT, speed, Direction.FORWARD)
#             sleep(50)
#           
#         motor_stop()
        
        if (line_sensor(LineSensor.M) == BLACK and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK and line_sensor(LineSensor.L1) == BLACK ):
            led_rgb(Color.VIOLET)
            motor_run(Motor.LEFT, speed, Direction.BACKWARD)
            sleep(1000)
            motor_stop()
            motor_run(Motor.RIGHT, speed, Direction.BACKWARD)
            sleep(1000)
            motor_stop()
           
def Edge():  # si on rencontre un bord, c'est à dire que M et R1 ne sont plus sur la ligne mais R2 si, on tourne à droite pour en "faire le tour" jusqu'à que R2 +R1 soient sur la ligne mais pas M 
    
    if (line_sensor(LineSensor.M) == WHITE and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == WHITE):
        led_rgb(Color.GREEN)
     
        
        while not line_sensor(LineSensor.R1) == BLACK:
            motor_run(Motor.LEFT, speed, Direction.FORWARD)
            
            sleep(50)
        
        

# Boucle principale 
while True :
    
    Tout_Droit()
    sleep(50)
    
    Coin()
    sleep(50)
    
    Edge()
    sleep(50)
