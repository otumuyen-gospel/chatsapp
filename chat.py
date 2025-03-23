from tkinter import *
class MainGui(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.createGui()
    def createGui(self):
        self.config(bg='#FFFFFF')
        self.pack(side='top', fill='both', expand='yes')
        self.topBar()
        self.leftBar()
        self.centerBar()

    def topBar(self):
        frame = Frame(self)
        frame.config(bg='#990000', pady=20)
        frame.pack(side='top', fill='x', expand='yes', anchor='n')
        Button(frame, text="welcome").pack()
    def leftBar(self):
        frame = Frame(self)
        frame.config(bg='#990000', padx=20)
        frame.pack(side='left', fill='both', expand='yes', anchor='n')
        Button(frame, text="welcome").pack()
    def centerBar(self):
        frame = Frame(self)
        frame.config(bg='blue')
        frame.pack(side='right', fill='both', expand='yes', anchor='n')
        Button(frame, text="welcome").pack()