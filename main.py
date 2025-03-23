from tkinter import *
from chat import *
class LoginGui(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.createGui()

    def createGui(self):
        self.config(bg='#990000')
        self.pack(side='top', fill='both', expand='yes')

        self.label = Label(self, text="ChatApp\nLogin")
        self.label.pack(side='top', fill='both', expand='yes')
        self.label.configure(font=('Verdana', 20, 'bold'), fg='white', pady=20, bg='#990000')

        frame = Frame(self)
        frame.pack(side='top', fill='both', expand='yes')
        frame.config(padx=450, pady=30, bg='#990000')
        frame.columnconfigure(0, weight=1)
        
        self.emailEntry = Entry(frame)
        self.emailEntry.grid(row=0,column=0, columnspan=2, sticky='nsew')
        self.emailEntry.config(bg='#990000', fg='white', bd=1, relief='raised')
        self.emailEntry.grid_configure(ipady=10, pady=2)
        self.emailEntry.focus_set()
        self.validEmailText = Label(frame, text="", bg='#990000', bd=0)
        self.validEmailText.grid(row=1,column=0, sticky='w')

        self.loginBtn = Button(frame, command=lambda : self.login(), text="Login")
        self.loginBtn.grid(row=2, column=0, sticky='nsew')
        self.loginBtn.config(bg='#990000', fg='white', bd=1, relief='raised', font=('Verdana', 10,'bold'))
        self.loginBtn.grid_configure(ipady=7, pady=25, ipadx=30)

        self.signupLink = Label(frame, text="A ONE TIME LOGIN - ENTER YOUR EMAIL")
        self.signupLink.grid(row=3, column=0, sticky='nsew')
        self.signupLink.config(bg='#990000', fg='white' , font=('Verdana', 10,'bold'))
        self.signupLink.grid_configure(ipady=7, pady=15, ipadx=30)

    
    def login(self):
        #remove this LoginGui and show the next interface
        if len(self.emailEntry.get()) > 1:
           self.label.config(text="Login Successful!")
           self.pack_forget()
           MainGui(self.master)
        else:
             self.validEmailText.config(text='please enter your email',fg='yellow')

window = Tk()
if __name__ == '__main__':
    window.title("ChatApp")
    container = Frame(window)
    container.pack(side='top', fill='both', expand='yes')
    LoginGui(container)
    window.mainloop()


