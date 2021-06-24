from tkinter import *
import time
import pygame

text_font = ("Boulder", 68, "bold")
text_font2 = ("Boulder", 16)
background = "#f2e750"
foreground = "#363529"
border_width = 25
alarms = []
stopped = False
started = False

pygame.mixer.init()
class Alarm():
    def __init__(self, name, alarm_time):
        self.name = name
        self.alarm_time = alarm_time
        
    def ring(self):
        global stopped
        for self in alarms:
            if time_live == self.alarm_time:
                if stopped == False:
                    pygame.mixer.music.load("ringtone.mp3")
                    pygame.mixer.music.play()
                    stopped = True
                    stop()
                    
                else:
                    pass
            else:
                pass

alarm1 = Alarm(None, None)

def main():
    global label
    app_window = Tk()
    app_window.title("Digital Clock App")
    app_window.geometry("420x300")
    app_window.resizable(1,1)
    app_window.configure(bg = "#f2e750")


    label = Label(
        app_window,
        font = text_font,
        bg = background,
        fg = foreground,
        bd = border_width)
    label.grid(row = 0, column = 1)

    alarm_bt = Button(
        app_window,
        text = "Set Alarm",
        font = text_font2,
        bg = "black",
        fg = "white",
        relief = FLAT,
        command = alarm_func

    )
    alarm_bt.grid(row = 1, column = 1, pady = 5)

    stopwatch_bt = Button(
        app_window,
        text = "Stopwatch",
        font = text_font2,
        bg = "black",
        fg = "white",
        relief = FLAT,
        command = stopwatch

    )
    stopwatch_bt.grid(row = 2, column = 1, pady = 5)

    timer_bt = Button(
        app_window,
        text = "Timer",
        font = text_font2,
        bg = "black",
        fg = "white",
        relief = FLAT,
        command = timer

    )
    timer_bt.grid(row = 3, column = 1)  

    digital_clock()
    app_window.mainloop()

def digital_clock():
    global time_live
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200, digital_clock)
    alarm1.ring()

def alarm_func():
    global alarm_win
    alarm_win = Toplevel()
    alarm_win.title("Digital Clock App")
    alarm_win.geometry("640x200")
    alarm_win.resizable(1,1)
    alarm_win.configure(bg = "#f2e750")

    global hour1, hour2, minutes1, minutes2, seconds1, seconds2

    hour1 = Spinbox(
        alarm_win,
        from_ = 0,
        to = 2,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    hour1.grid(row = 0, column = 1, pady = 24, padx = 10)

    hour2 = Spinbox(
        alarm_win,
        from_ = 0,
        to = 9,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    hour2.grid(row = 0, column = 2, pady = 24)

    labeldot = Label(
        alarm_win,
        font = text_font,
        bg = background,
        fg = foreground,
        text = ":"
    )
    labeldot.grid(row = 0, column = 3, pady = 24)

    minutes1 = Spinbox(
        alarm_win,
        from_ = 0,
        to = 5,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    minutes1.grid(row = 0, column = 4, pady = 24, padx = 10)

    minutes2 = Spinbox(
        alarm_win,
        from_ = 0,
        to = 9,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    minutes2.grid(row = 0, column = 5, pady = 24)

    labeldot2 = Label(
        alarm_win,
        font = text_font,
        bg = background,
        fg = foreground,
        text = ":"
    )
    labeldot2.grid(row = 0, column = 6, pady = 24)

    seconds1 = Spinbox(
        alarm_win,
        from_ = 0,
        to = 5,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    seconds1.grid(row = 0, column = 7, pady = 24, padx = 10)

    seconds2 = Spinbox(
        alarm_win,
        from_ = 0,
        to = 9,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    seconds2.grid(row = 0, column = 8, pady = 24)

    set_bt = Button(
        alarm_win,
        text = "Set",
        font = text_font2,
        bg = "black",
        fg = "white",
        relief = FLAT,
        command = create_alarm
        )
    set_bt.grid(row = 1, column = 4)

    var = StringVar()
    var.set(time_live[0])
    hour1.config(textvariable=var)
    var = StringVar()
    var.set(time_live[1])
    hour2.config(textvariable=var)

    var = StringVar()
    var.set(time_live[3])
    minutes1.config(textvariable=var)
    var = StringVar()
    var.set(time_live[4])
    minutes2.config(textvariable=var)

    var = StringVar()
    var.set(time_live[6])
    seconds1.config(textvariable=var)
    var = StringVar()
    var.set(time_live[7])
    seconds2.config(textvariable=var)


def create_alarm():
    global alarm1, alarms
    a = hour1.get() + hour2.get() + ":" + minutes1.get() + minutes2.get() + ":" + seconds1.get() + seconds2.get()
    alarm1 = Alarm("alarm", a)
    alarms.append(alarm1)
    alarm_win.destroy()
    print(alarms)

def timer():
    global timer_app, frame
    timer_app = Toplevel()
    timer_app.configure(bg = background)
    timer_app.title("Timer")

    frame = Frame(
        timer_app,
        bg = background
    )
    frame.pack()

    global hour1, hour2, minutes1, minutes2, seconds1, seconds2

    hour1 = Spinbox(
        frame,
        from_ = 0,
        to = 2,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    hour1.grid(row = 0, column = 1, pady = 24, padx = 10)

    hour2 = Spinbox(
        frame,
        from_ = 0,
        to = 9,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    hour2.grid(row = 0, column = 2, pady = 24)

    labeldot = Label(
        frame,
        font = text_font,
        bg = background,
        fg = foreground,
        text = ":"
    )
    labeldot.grid(row = 0, column = 3, pady = 24)

    minutes1 = Spinbox(
        frame,
        from_ = 0,
        to = 5,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    minutes1.grid(row = 0, column = 4, pady = 24, padx = 10)

    minutes2 = Spinbox(
        frame,
        from_ = 0,
        to = 9,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    minutes2.grid(row = 0, column = 5, pady = 24)

    labeldot2 = Label(
        frame,
        font = text_font,
        bg = background,
        fg = foreground,
        text = ":"
    )
    labeldot2.grid(row = 0, column = 6, pady = 24)

    seconds1 = Spinbox(
        frame,
        from_ = 0,
        to = 5,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    seconds1.grid(row = 0, column = 7, pady = 24, padx = 10)

    seconds2 = Spinbox(
        frame,
        from_ = 0,
        to = 9,
        wrap = True,
        font = ("Boulder", 50, "bold"),
        width = 1
    )
    seconds2.grid(row = 0, column = 8, pady = 24)


    start_bt = Button(
        frame,
        text = "Start",
        font = text_font2,
        bg = "black",
        fg = "white",
        relief = FLAT,
        command = get_time
        )
    start_bt.grid(row = 1, column = 4)

    timer_app.mainloop()

def get_time():
    global b, total, timer_time, time_left
    b = hour1.get() + hour2.get() + ":" + minutes1.get() + minutes2.get() + ":" + seconds1.get() + seconds2.get()
    total = int(hour1.get() + hour2.get()) * 3600 + int(minutes1.get() + minutes2.get()) * 60 + int(seconds1.get() + seconds2.get())
    frame.destroy()
    timer_time = Label(
        timer_app,
        text = str(b),font = text_font,
        bg = background,
        bd = border_width,
        fg = foreground
    )
    timer_time.grid(row = 0, column = 1)
    time_left = total
    start_timer()


def start_timer():
    global total, time_left
    time_left -= 1
    hours = int(time_left / 3600)
    minutes = int((time_left - hours * 3600) / 60)
    seconds = int(time_left - hours * 3600 - minutes * 60)
    time_left = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    timer_time.config(text = time_left)
    time_left = hours * 3600 + minutes * 60 + seconds
    if time_left > 0:
        timer_time.after(1000, start_timer)
    else:
        pygame.mixer.music.load("C:/Users/rares/OneDrive/Desktop/python_curs/lectia 20(modul 2)/ringtone.mp3")
        pygame.mixer.music.play(loops = 0)
        stop()


def stop():
    global stop_win
    stop_win = Toplevel()
    stop_win.configure(bg = background)
    stop_win.title("Ringing")

    stop_bt = Button(
        stop_win,
        text = "Stop",
        command = stop_ringtone,
        bg = "red"
    )
    stop_bt.pack()

def stop_ringtone():
    global stopped
    pygame.mixer.music.stop()
    stop_win.destroy()
    stopped = False

def stopwatch():
    global stopwatch_app, start_stop, timer2

    stopwatch_app = Toplevel()
    stopwatch_app.configure(bg = background)
    stopwatch_app.geometry("420x250")

    global hours, minutes, seconds, time_done
    hours = 0
    minutes = 0
    seconds = 0
    time_done = hours * 3600 + minutes * 60 + seconds

    timer2 = Label(
        stopwatch_app,
        text = str(hours) + ":" + str(minutes) + ":" + str(seconds),
        font = text_font,
        bg = background
    )
    timer2.pack(padx = 15)

    start_stop = Button(
        stopwatch_app,
        text = "Start",
        bg = "green",
        command = start_pause,
        relief = FLAT,
        font = text_font2
    )
    start_stop.pack(pady = 10)

    reset = Button(
        stopwatch_app,
        text = "Reset",
        fg = "white",
        bg = "black",
        relief = FLAT,
        font = text_font2,
        command = reset_func
    )
    reset.pack()


def start_pause():
    global started
    if started == False:
        started = True
        start_stop.config(text = "Stop", bg = "red")
        start_stopwatch()
    else:
        started = False
        start_stop.config(text = "Start", bg = "green")

def start_stopwatch():
    if started:
        global hours, minutes, seconds, time_done
        time_done += 1
        hours = int(time_done / 3600)
        minutes = int((time_done - hours * 3600) / 60)
        seconds = int(time_done - hours * 3600 - minutes * 60)
        time_done = str(hours) + ":" + str(minutes) + ":" + str(seconds)
        timer2.config(text = time_done)
        time_done = hours * 3600 + minutes * 60 + seconds
        timer2.after(1000, start_stopwatch)

def reset_func():
    stopwatch_app.destroy()
    stopwatch()

main()
