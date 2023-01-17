from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for move2 in range(7):  
    robotArm.grab()
    for move3 in range(8):   
        robotArm.moveRight()
    robotArm.drop()
    for move4 in range(8):
        robotArm.moveLeft()
    
robotArm.wait()