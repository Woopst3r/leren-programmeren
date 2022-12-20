count = 0
startnum = 50
som = startnum + count
while startnum <= 2000:
    if startnum > 1000:
        break
    print (startnum)
    count += 1
    startnum = som + startnum + count
print ("einde")