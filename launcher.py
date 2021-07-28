import tkinter
from PIL import Image, ImageTk
import pyglet, time_gui as tg
from tkcalendar import Calendar, DateEntry
import notify

def notify_now():
    global tg, view, title_input, note_input
    notify.notifier(title_input.get(), note_input.get(), time_module.get_time())

def on_enter(e):
    reminder.config(background='#ee062e',foreground='white')
def on_leave(e):
    reminder.config(background='#cc062e',foreground='white')

view = tkinter.Tk()#logic start
view.title('Notify')#title bar title
view.iconbitmap(r'./pictures/N.ico')#Title bar icon

#loaded fonts
pyglet.font.add_file("./fonts/Chopsic-K6Dp.ttf")
pyglet.font.add_file("./fonts/Oasis-BW0JV.ttf")

#parameters for the window
view.geometry("300x530")
view.minsize(250,350)
view.maxsize(715,1275)

#Label for title heading
title_label = tkinter.Label(view,text='Notify',
                            background='#191970',
                            fg='#13F4EF',
                            font=('oasis', 30),
                            )
title_label.pack()

#loaded background image
bg_img = Image.open('./pictures/led.png')
bg_img = ImageTk.PhotoImage(bg_img)
view.configure(bg='#191970')

#Creation of label and input box for title
title_input= tkinter.StringVar()
title_label = tkinter.Label(view, text='Title', background='#191970',
                            fg='#CCFF02',
                            font=('chopsic', 18))
title_label.pack()
title = tkinter.Canvas(view, width=125, height=17)
title.pack()
entry1 = tkinter.Entry(view, textvariable=title_input )
entry1.config({"background":"#fdd7e4"})
#entry1.grid(column=1)
title.create_window(65, 9, window = entry1)

#Creation of label and input box for note
note_input=tkinter.StringVar()
title_label = tkinter.Label(view, text='Note', background='#191970',
                            fg='#CCFF02',
                            font=('chopsic', 18))
title_label.pack()
note = tkinter.Canvas(view, width=125, height=17)
note.pack()
entry2 = tkinter.Entry(view, textvariable=note_input)
entry2.config({"background":"#fdd7e4"})
#entry2.grid(column=1)
note.create_window(65, 9, window = entry2)

#Time selector
time_module = tg.Time(view)
time_module.pack()

#Reminder button
reminder = tkinter.Button( text='Set Reminder',
                         command=notify_now,
                         background='#Ac143c',
                         border='0',
                         font=('chopsic',13),
                         fg='white',
                         relief='flat',
                         activebackground = "#CCFF02"
                         )
note.create_window(200,180,window=reminder)
reminder.pack(fill=tkinter.X, expand=tkinter.YES, side='bottom')
reminder.bind('<Enter>', on_enter)#changes color of button upon hover
reminder.bind('<Leave>', on_leave)#changes color of button upon leave

image_label = tkinter.Label(view, image=bg_img)#background img placed at end
image_label.pack(fill=tkinter.BOTH, expand=tkinter.YES)

view.mainloop()#logic end