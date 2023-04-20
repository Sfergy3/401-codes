import os, time
from datetime import datetime, timedelta

#   create a while loop for the sensor tool.
while True:
    def checkstat(target): 
        response = os.system("ping -c 1 " + target)
    #ping target and set responses
        if response == 0:
            upstate = "I'm up, they see me"
        else:
            upstate = "I'm down"
        return upstate
    #call the function 
    upstate = checkstat("8.8.8.8")
    print(upstate)
    #delay loop for 2 seconds
    time.sleep(2) 
    #display the current time, tutorial for this found on realpython.com and tylers code screensharing
    now = datetime.now()
    print (now)
