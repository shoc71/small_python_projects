import tkinter as tk
import datetime
import time

class AlarmClock:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")
        
        self.alarm_time = None

        self.time_label = tk.Label(master, font=("Arial", 30))
        self.time_label.pack()

        self.set_alarm_button = tk.Button(master, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack()

        self.cancel_button = tk.Button(master, text="Cancel", command=self.cancel_alarm)
        self.cancel_button.pack()
        self.cancel_button.config(state=tk.DISABLED)

    def set_alarm(self):
        self.alarm_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
        self.set_alarm_button.config(state=tk.DISABLED)
        self.cancel_button.config(state=tk.NORMAL)
        self.update_time()

    def cancel_alarm(self):
        self.alarm_time = None
        self.set_alarm_button.config(state=tk.NORMAL)
        self.cancel_button.config(state=tk.DISABLED)
        self.update_time()

    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)

        if self.alarm_time is not None:
            remaining_time = self.alarm_time - datetime.datetime.now()
            if remaining_time.total_seconds() <= 0:
                self.alarm()
            else:
                self.master.after(1000, self.update_time)

    def alarm(self):
        self.master.bell()
        self.alarm_time = None
        self.set_alarm_button.config(state=tk.NORMAL)
        self.cancel_button.config(state=tk.DISABLED)

root = tk.Tk()
clock = AlarmClock(root)
clock.update_time()
root.mainloop()
