from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
moveright = 10
moveleft = 9

for move2 in range(5):
    robotArm.grab()
    for moveright in range(moveright - 1):
        robotArm.moveRight()
    robotArm.drop()
    for moveleft in range(moveleft - 1):
        robotArm.moveLeft()  
robotArm.wait()