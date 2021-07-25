from plyer import notification
import time
import datetime

title=input("Title: ")
if title == "":
    title = 'Reminder'
message=input('Throw a/c water and go to sleep')
if message == '':
    message = 'Alarm'
at_time = input("Time (HH:MM:SS) (SS is optional): ")
if at_time == '':
    at_time='22:49'


weekly = input("Daily (1/0): ")
if weekly == '':
    weekly = 0
else:
    weekly = int(weekly)

while(True):
    if(time.strftime('%H:%M')==at_time):
        notification.notify(
            title=title,
            message=message,
            app_icon='sleep_icon_154827.ico',
            timeout=10,
            toast=False
        )
        if weekly==0:
            exit(1)

    time.sleep(60)