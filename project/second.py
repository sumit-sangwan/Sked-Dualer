from tkinter import *
import tkinter as tk
# from datetime import date
# from time import strftime

class second:
    def __init__(self):
        self.mainSecond()

    def mainSecond(self):
        self.newwindow = tk.Tk()
        self.newwindow.geometry('800x500')
        self.newwindow.title('Sked Dualer')

        tk.Label(self.newwindow, text="--------------------------------------------", font=("Arial",40)).place(x=0,y=20)

        

        self.newwindow.mainloop()

if __name__ == "__main__":
    second()