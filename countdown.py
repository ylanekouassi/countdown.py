#COUNTDOWN TIMER

import time

insert_time = int(input("Enter the time in second: "))

for i in range(insert_time, 0, -1):
    time.sleep(1)
    seconds = i % 60 
    minutes = int(i / 60) % 60 # 1 minutes = 60 sec. 
    print(f"{minutes} : {seconds}")