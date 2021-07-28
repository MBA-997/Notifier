from plyer import notification
import time
import datetime

def notifier(_title, note, time_given):
    title = _title
    message = note
    at_time = time_given

    if title == "":
        title = 'Reminder'
    if message == '':
        message = 'Alarm'
    if at_time == '':
        at_time='22:49'

    weekly = ''
    if weekly == '':
        weekly = 0
    else:
        weekly = int(weekly)

    (hour, minute) = at_time.split(":")
    hour=int(hour)
    minute=int(minute)

    while(True):

        if(time.strftime('%H:%M')==at_time):
            notification.notify(
                title=title,
                message=message,
                app_icon='./pictures/sleep_icon_154827.ico',
                timeout=10,
                toast=False
            )
            if weekly==0:
                exit(1)
        
        #Subtracts time from given time to find sleeping time
        minute = minute-int(time.strftime('%M'))
        hour = hour-int(time.strftime('%H'))

        #If minutes are negative add 60 to find real time for sleeping
        if minute<0:
            minute = 60 + minute
        if hour<0:
            hour = 24 + hour

        time.sleep(minute*60)
        if hour>1 or minute==0:
            time.sleep(hour*60*60)
