from tkinter import *
from login import *
class forgotGui(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack(side='top', fill='both', expand='yes')
        self.config(bg='blue')
        btn = Button(self, command= lambda : self.gotoConfirm(), text="Confirm Email")
        btn.pack()

    def gotoConfirm(self):
        #remove this SignupGui and show the next interface
        self.pack_forget()
        LoginGui(self.master)
