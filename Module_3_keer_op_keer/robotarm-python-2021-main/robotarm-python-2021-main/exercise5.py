from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')
robotArm.speed= 3
# Jouw python instructies zet je vanaf hier:

for move in range(7):
    robotArm.moveRight()
for move2 in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    if move2 < 7:
        robotArm.moveLeft()
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()