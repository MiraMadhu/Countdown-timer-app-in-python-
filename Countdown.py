import tkinter as tk

def start_countdown():
    try:
        t = int(entry.get())
        countdown(t)
    except ValueError:
        time_var.set("Invalid input")

def countdown(t):
    if t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time_var.set(timer)
        root.update()
        root.after(1000, countdown, t-1)
    else:
        time_var.set("Fire in the hole!!")

root = tk.Tk()
root.title("Countdown Timer")

time_var = tk.StringVar()
time_var.set("00:00")

label = tk.Label(root, textvariable=time_var, font=("Helvetica", 48))
label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 24))
entry.pack(pady=20)
entry.insert(0, "Enter time in seconds")

start_button = tk.Button(root, text="Start Countdown", command=start_countdown, font=("Helvetica", 24))
start_button.pack(pady=20)

root.mainloop()
