from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
moveright = 10
moveleft = 9
robotArm.grab()
for move2 in range(5):
    for move3 in range(1):
        for moveright in range(moveright - 1):
            robotArm.moveRight()
        robotArm.drop()
        for moveleft in range(moveleft - 1):
            robotArm.moveLeft()
    if move2 <4:   
        robotArm.grab()
robotArm.wait()