from RobotArm import RobotArm

robotArm = RobotArm('exercise 1')

stap = 9
for x in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    if robotArm._color == "red":    
        for x in range(0,stap):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(0,stap):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
    stap -=1

robotArm.scan() 
robotArm.wait()