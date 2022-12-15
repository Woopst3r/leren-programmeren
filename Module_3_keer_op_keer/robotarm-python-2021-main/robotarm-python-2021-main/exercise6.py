from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
for move2 in range(3):   
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop() 
    if move2 < 5:
        robotArm.moveLeft()


    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()