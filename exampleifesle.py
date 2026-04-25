# alarmtime = input("Enter the current time (HH:MM:SS):")
# currenttime = "6:30:00 AM"
# 
# if (currenttime == alarmtime):
    # print("alarm plays, its time wake up!")
# else:
 # print("alarm dont plays, its not the time to wake up") 
# 
# print("good morning ,its the day begins..") 

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
