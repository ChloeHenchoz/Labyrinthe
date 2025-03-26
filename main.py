"projet labyrinthe 26.03.2025, Natasha et Chloé"
from maprincess import *
from microbit import *

#constantes
# pince = 0.1
WHITE = 0
BLACK = 1
# pince = 0.1
speed = 40

print("depart")

while True :
    sleep(100)
    print("boucle")
    if line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==WHITE and line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.M)==WHITE :
        motor_run(Motor.LEFT, speed, Direction.FORWARD)
        motor_run(Motor.RIGHT, speed, Direction.FORWARD)
        print("je roule")
        
    if line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.M)==BLACK :
        motor_stop()
        print("je je")
    
    

