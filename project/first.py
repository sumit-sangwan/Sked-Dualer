from tkinter import *
import tkinter as tk
from datetime import date
from time import strftime
import second as second

class first:
    def __init__(self):
        self.mainfront()

    def start(self):
        self.window.destroy()
        second.second()

    def mainfront(self):
        self.window = tk.Tk()
        self.window.geometry('800x500')
        self.window.title('Sked Dualer')
        bgColor='#fff'
        self.window.configure(bg='#fff')
        
        filePath = "img/logotemp1.png"
        logo = tk.PhotoImage(file=filePath)
        tk.Label(self.window, image=logo, background=bgColor).place(x=100,y=20)
        
        lbl = Label(self.window, font = ('calibri', 40, 'bold'),background = bgColor,foreground = '#0E6F00')
        lbl.place(x=200,y=200)
        string = strftime('%H:%M %p')
        lbl.config(text = string)
        # lbl.after(1000)

        tk.Label(self.window, text="The only software", font=("Arial",12), background=bgColor, foreground='#111').place(x=600,y=150)
        tk.Label(self.window, text="you need to", font=("Arial",12), background=bgColor, foreground='#111').place(x=622,y=175)
        tk.Label(self.window, text="keep track of", font=("Arial",12), background=bgColor, foreground='#111').place(x=617,y=200)
        tk.Label(self.window, text="your day.", font=("Arial",12), background=bgColor, foreground='#111').place(x=630,y=225)
        tk.Label(self.window, text="Select the date", font=("Arial",12), background=bgColor, foreground='#111').place(x=605,y=250)
        tk.Label(self.window, text="and start scheduling.", font=("Arial",12), background=bgColor, foreground='#111').place(x=592,y=275)
        
        tk.Button(self.window, text="Start scheduling!", font=("Arial", 14), bd=0, activebackground='#0E6F00', activeforeground=bgColor, fg=bgColor, background='#15AD00', command=self.start).place(x=50,y=400,height=50,width=500)
        
        today = date.today()

        datesOp = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
        dataVar = StringVar()
        dataVar.set(today.strftime("%d"))
        date1 = tk.OptionMenu(self.window , dataVar, *datesOp)
        date1.config(font=("Arial",12), bd=0, activebackground='#0E6F00', activeforeground=bgColor, fg=bgColor, background='#15AD00')
        date1.place(x=600,y=400,height=50,width=80)
        
        monthsOp = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        monthVar = StringVar()
        monthVar.set(today.strftime("%B"))
        month1 = tk.OptionMenu(self.window, monthVar, *monthsOp)
        month1.config(font=("Arial",12), bd=0, activebackground='#0E6F00', activeforeground=bgColor, fg=bgColor, background='#15AD00')
        month1.place(x=650,y=400,height=50,width=100)

        tk.Label(self.window, background=bgColor).place(x=725,y=400,height=50,width=50)


        self.window.mainloop()

if __name__ == "__main__":
    page = first()