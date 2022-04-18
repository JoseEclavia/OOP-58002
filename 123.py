from tkinter import *
win = Tk()
win.geometry("300x200+10+20")
win.title('Label')

#1
lbl = Label(win,text = "Laboratory Activity 5 \n Submitted to: Mam Sayo")
lbl.place(x=80, y=30)

#2
txtfld = Entry(win, font= "Bold")
txtfld.place(x=50, y=80)

#3
fthr = Label(win,text = "Charles Babbage",font='Italic', bg = "cyan")
fthr.place(x=90, y=120)

win.mainloop()

