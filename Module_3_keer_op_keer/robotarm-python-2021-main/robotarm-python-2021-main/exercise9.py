from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for move2 in range(4):
    for move3 in range(move2 + 1):
        robotArm.grab()
        for move4 in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for move4 in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()