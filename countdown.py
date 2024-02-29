#COUNTDOWN TIMER

import time

insert_time = int(input("Enter the time in second: "))

for i in range(insert_time, 0, -1):
    time.sleep(1)
    seconds = i % 60 
    minutes = int(i / 60) % 60 # 1 minutes = 60 sec. 
    hours = int(i / 3600) # 1 hour = 3600 sec.
    print(f"{hours:02} : {minutes:02} : {seconds:02}") #formatted time, 2 digits will be displayed