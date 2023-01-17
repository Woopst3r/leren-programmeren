from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')
robotArm.speed=3

# Jouw python instructies zet je vanaf hier:
for y in range(5):
    robotArm.moveRight()
    for move2 in range(6):   
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
    if y != 4:
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()