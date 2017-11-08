
from datetime import datetime
import time

currentDate = datetime.now()
currentTime = currentDate.hour

openTime = 9
closeTime = 21

londonTime = currentTime + 8
nycTime = currentTime + 3


## Portland
if currentTime >= openTime and currentTime < closeTime:
    print("Portland is open...\n")
    time.sleep(2)
else:
    print("Portland is closed...\n")
    time.sleep(2)

## London (+8:00h)
if londonTime >= openTime and londonTime < closeTime:
    print("London is open...\n")
    time.sleep(2)
else:
    print("London is closed...\n")
    time.sleep(2)


## NYC (+3:00h)
if nycTime >= openTime and nycTime < closeTime:
    print("New York is open...\n")
    time.sleep(2)
else:
    print("New York is closed...\n")
    time.sleep(2)



