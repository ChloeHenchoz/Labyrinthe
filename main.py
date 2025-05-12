"""Projet Laby 04.05.25 """
#Imports

from maprincess import *
from microbit import *
import radio

# Start radio module #
radio.config(channel=7, address=50)
radio.on()
        
    
#Constantes

WHITE = 0
BLACK = 1
speed = 20

#Définitions

def Tout_Droit(): # Tant que R2 + R1 sont sur la ligne et que M n'y est pas, on avance jusqu'à que M arrive sur une ligne (j'ai enlevé la condition pour L1 qui contribuait au bug je crois) 
    
    if (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==BLACK ):
        led_rgb(Color.WHITE)
        
        while (line_sensor(LineSensor.M)== WHITE and line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==BLACK):
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
        
        while (line_sensor_all() == (1, 1, 0, 1, 0)):
            led_rgb(Color.RED)
            motor_run(Motor.ALL, speed, Direction.BACKWARD)
            sleep(50)
        motor_stop()
            
            
    
def Coin(): # si M + R1 + R2 sont sur une ligne, ce qui devrait être un coin, on tourne sur place jusqu'à que M ne soit plus sur la ligne
    
    if (line_sensor(LineSensor.M) == BLACK and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == BLACK):
        led_rgb(Color.BLUE)
         
        while not line_sensor(LineSensor.M) == WHITE:
            print("BACKWARD")
            print(line_sensor_all())
            motor_run(Motor.LEFT, speed, Direction.BACKWARD)
            motor_run(Motor.RIGHT, speed, Direction.FORWARD)
            sleep(50)
        
        
        print("stop")
        print(line_sensor_all())
        motor_stop()
        
        if (line_sensor_all() == (0, 1, 0, 0, 0) or line_sensor_all() == (1, 1, 0, 0, 0) or line_sensor_all() == (0, 1, 0, 1, 1)): #  dans les deux config qui font que le robot s'arrête completement, on le fait reculer un peu pour qu'il reparte ( imite un coup de pouce) 
           motor_run(Motor.ALL, speed, Direction.BACKWARD)
           sleep(100)
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
           
        while (line_sensor_all() == (1, 1, 0, 1, 0)):
            led_rgb(Color.VIOLET)
            motor_run(Motor.ALL, speed, Direction.BACKWARD)
            sleep(50)
        motor_stop()
            
def Edge():  # si on rencontre un bord, c'est à dire que M et R1 ne sont plus sur la ligne mais R2 si, on tourne à droite pour en "faire le tour" jusqu'à que R2 +R1 soient sur la ligne mais pas M 
    
    if (line_sensor(LineSensor.M) == WHITE and line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.R1) == WHITE):
        led_rgb(Color.GREEN)
        print("green")
     
        
        while not line_sensor(LineSensor.R1) == BLACK:
            motor_run(Motor.LEFT, speed, Direction.FORWARD)
            
            sleep(50)
        
def Fini():
    if 3 < ultrasonic() < 6 :
        Run = False
        radio.send_bytes(bytes(0))
        
        

def Radio_check():
    
    new_trame = radio.receive_bytes()
    if new_trame:
        msgRecu = trame_to_msg(new_trame, userId)
        return msgRecu 

        

Run = True 

# Boucle principale 
while True :
    
    while Run == True:
    
        Tout_Droit()
        sleep(50)
        
        Coin()
        sleep(50)
        
        Edge()
        sleep(50)
        
        Fini()
        
    if Radio_check() == 0:  # Il faudrait faire commencer le deuxième robot en Run == False 
            Run = True 
    
        
    
    
