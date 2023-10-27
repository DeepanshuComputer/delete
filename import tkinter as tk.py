import tkinter as tk
import time

class ClockApp(tk.Tk):
    def __init__(self):
        super().__init__()

        
        self.time_label = tk.Label(self, text="00:00:00", font=("Arial", 60))
        self.time_label.pack()

        
        self.update_time()

    def update_time(self):
        
        current_time = time.strftime("%H:%M:%S")

        
        self.time_label.config(text=current_time)

        
        self.after(1000, self.update_time)

if __name__ == "__main__":
    app = ClockApp()
    app.mainloop()