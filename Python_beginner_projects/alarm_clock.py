#Alarm clock......

import datetime

current_hr=datetime.datetime.today().strftime("%H")
current_min=datetime.datetime.today().strftime("%M")
str=datetime.datetime.today().strftime("%H:%M")
print("The time right now : "+str)
hr=int(input("enter the hour at which the alarm should raise : "))
min=int(input("enter the minute at which the alarm should raise : "))
while True:
    if (hr==int(datetime.datetime.today().strftime("%H")) & min==int(datetime.datetime.today().strftime("%M"))):
        print("Alarm now.....")
        break
    else:
        print("No Alarm.....")
        break
