from tkinter import *
from login import *
class SignupGui(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.createGui()

    def createGui(self):
        self.config(bg='#990000')
        self.pack(side='top', fill='both', expand='yes')

        self.label = Label(self, text="New Account")
        self.label.pack(side='top', fill='both', expand='yes')
        self.label.configure(font=('Verdana', 20, 'bold'), fg='white', pady=20, bg='#990000')

        frame = Frame(self)
        frame.pack(side='top', fill='both', expand='yes')
        frame.config(padx=450, pady=40, bg='#990000')
        frame.columnconfigure(0, weight=1)


        self.signupLink = Label(frame, text="GOTO LOGIN INSTEAD")
        self.signupLink.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.signupLink.config(bg='#990000', fg='white', cursor='hand2' , 
                               font=('Verdana', 10,'bold'))
        self.signupLink.grid_configure(ipady=7, pady=25, ipadx=30)
        self.signupLink.bind("<Button-1>", (lambda event:self.login()))
        self.signupLink.bind("<Enter>", (lambda event :self.mouseEnter()))
        self.signupLink.bind("<Leave>", (lambda event :self.mouseLeave()))

        labelEmail = Label(frame, text="EMAIL ADDRESS")
        labelEmail.grid(row=1,column=0,columnspan=2, sticky='w')
        labelEmail.config(bg='#990000', fg='white')
        labelEmail.grid_configure(ipady=7, pady=2)
        labelEmail.configure(font=('Verdana', 11, 'bold'))
        self.emailEntry = Entry(frame)
        self.emailEntry.grid(row=2,column=0, columnspan=2, sticky='nsew')
        self.emailEntry.config(bg='#990000', fg='white', bd=1, relief='raised')
        self.emailEntry.grid_configure(ipady=10, pady=2)
        self.emailEntry.focus_set()
        self.validEmailText = Label(frame, text="", bg='#990000', bd=0)
        self.validEmailText.grid(row=3,column=0,columnspan=2, sticky='w')


        labelPass = Label(frame, text="PASSWORD")
        labelPass.grid(row=4,column=0, columnspan=2, sticky='w')
        labelPass.config(bg='#990000', fg='white')
        labelPass.grid_configure(ipady=7, pady=2)
        labelPass.configure(font=('Verdana', 11, 'bold'))
        self.passEntry = Entry(frame, show='*')
        self.passEntry.grid(row=5,column=0, columnspan=2, sticky='nsew')
        self.passEntry.config(bg='#990000', fg='white', bd=1, relief='raised')
        self.passEntry.grid_configure(ipady=10, pady=2)
        self.validPassText = Label(frame, text="", bg='#990000',bd=0)
        self.validPassText.grid(row=6,column=0,columnspan=2, sticky='w')


        self.loginBtn = Button(frame, command=lambda : self.login(), text="Signup")
        self.loginBtn.grid(row=7, column=0, columnspan=1, sticky='w')
        self.loginBtn.config(bg='#990000', fg='white', bd=1, relief='raised', font=('Verdana', 10,'bold'))
        self.loginBtn.grid_configure(ipady=7, pady=25, ipadx=30)

        self.forgotLink = Label(frame, text="Forgot Password?")
        self.forgotLink.grid(row=7, column=1, columnspan=1, sticky='e')
        self.forgotLink.config(bg='#990000', fg='white', cursor='hand2',font=('Verdana', 10,'bold'))
        self.forgotLink.grid_configure(ipady=7, pady=25, ipadx=30)
        self.forgotLink.bind("<Button-1>", (lambda event :self.forgot()))
        self.forgotLink.bind("<Enter>", (lambda event :self.mouseEnter2()))
        self.forgotLink.bind("<Leave>", (lambda event :self.mouseLeave2()))

    
    def mouseEnter(self):
        self.signupLink.config(fg='#CCC')
    def mouseLeave(self):
        self.signupLink.config(fg='white')
    def mouseEnter2(self):
        self.forgotLink.config(fg='#CCC')
    def mouseLeave2(self):
        self.forgotLink.config(fg='white')
    def signup(self):
        #remove this LoginGui and show the next interface
        if len(self.emailEntry.get()) > 1:
             if len(self.passEntry.get()) > 1:
                #remove this LoginGui and show the next interface
                self.label.config(text="Login Successful!")
                self.pack_forget()
                self.login()
             else:
                 self.validPassText.config(text='please enter your password',fg='yellow')
        else:
             self.validEmailText.config(text='please enter your email',fg='yellow')
    def login(self):
        #remove this LoginGui and show the next interface
        self.pack_forget()
        LoginGui(self.master)
    def forgot(self):
        #remove this SignupGui and show the next interface
        self.pack_forget()
        forgotGui(self.master)