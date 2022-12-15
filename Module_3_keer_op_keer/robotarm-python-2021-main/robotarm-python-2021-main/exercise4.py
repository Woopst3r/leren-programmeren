from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:

for move in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    if move < 4:
        robotArm.moveLeft()
        robotArm.moveLeft()
for move2 in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    if move < 4:
        robotArm.moveLeft()
        

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()