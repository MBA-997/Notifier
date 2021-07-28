import tkinter as tk
import time

class Time(tk.Frame):
    #Creates time wheel using spinbox
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr=tk.StringVar(self,time.strftime('%H'))
        self.hourstr.trace("w",self.trace_time)
        self.hour = tk.Spinbox(self,from_=0,to=23,wrap=True,
                                textvariable=self.hourstr,width=10,state="readonly")

        self.minstr=tk.StringVar(self,time.strftime('%M'))
        self.minstr.trace("w",self.trace_time)
        self.last_value = "none"
        self.min = tk.Spinbox(self,from_=0,to=59,wrap=True,
                                textvariable=self.minstr,width=10,state="readonly",
                                background='#000000',fg='black',)
        self.hour.grid()
        self.min.grid(row=0,column=1)
        

    #Traces time to check if value is out of bound and corrects accordingly
    def trace_time(self,*args):
        try:
            if self.last_value == "59" and self.minstr.get() == "0":
                self.hourstr.set(int(self.hourstr.get())+1 if self.hourstr.get() !="23" else 0)
            self.last_value = self.minstr.get()
        except Exception as e:
            print()

 
    #Return current time selected by user
    def get_time(self):
        self.trace_time()#Updates time if necessary
        hr=self.hourstr.get()
        min=self.minstr.get()

        #Adds zeros for format
        if(len(hr)<2):
            hr='0'+hr
        if(len(min)<2):
            min='0'+min
        
        #Concat of hour and minute
        full_time=(hr+':'+min)
        return full_time