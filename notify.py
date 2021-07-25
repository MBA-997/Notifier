from plyer import notification
import time

title= 'Psst...Reminder'
message='Throw a/c water and go to sleep'
while(True):
    if(time.strftime('%H:%M')=='16:42'):
        notification.notify(
            title=title,
            message=message,
            app_icon='sleep_icon_154827.ico',
            timeout=10,
            toast=False
        )
        exit(1)
    time.sleep(60)