from multiprocessing import Event

countdown = int(input("Fanaf waneer wil je dat de raket af telt?: "))
for tafels in range (countdown):
    Event().wait(1)   
    (countdown -1)    
    print (countdown - tafels)
print ("Lift off!!!")
    
