from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')

stap = 8
for x in range(stap):
    robotArm.grab()
    color = robotArm.scan()
    if robotArm._color == "white":
        robotArm.moveRight()
    robotArm.drop()
    robotArm.moveRight()

robotArm.wait()