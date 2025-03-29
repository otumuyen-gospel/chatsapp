from tkinter import *
from chat import *
class LoginGui(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.createGui()

    def createGui(self):
        self.pack(side='top', fill='both', expand='yes')

        self.label = Label(self, text="Chat App\nLogin")
        self.label.pack(side='top', fill='both', expand='yes')
        self.label.configure(font=('Verdana', 20, 'bold'), fg='white', pady=20, bg='purple')

        frame = Frame(self)
        frame.pack(side='top', fill='both', expand='yes')
        frame.config(padx=450, pady=30, bg='#FFFFFF')
        frame.columnconfigure(0, weight=1)
        
        self.emailLabel = Label(frame, text="Email Address")
        self.emailLabel.grid(row=0, column=0, sticky='e')
        self.emailLabel.config(bg='#FFFFFF', fg='#333' , font=('Verdana', 10,'bold'))
        self.emailEntry = Entry(frame)
        self.emailEntry.grid(row=1,column=0, sticky='nsew')
        self.emailEntry.config(bg='white', bd=0, relief='sunken',font=('Verdana', 10,'normal'))
        self.emailEntry.grid_configure(ipady=10, pady=2)
        self.emailEntry.focus_set()
        self.validEmailText = Label(frame, text="", bg='#FFFFFF', bd=0)
        self.validEmailText.grid(row=2,column=0, sticky='w')

        self.loginBtn = Button(frame, command=lambda : self.login(), text="Login")
        self.loginBtn.grid(row=3, column=0, sticky='nsew')
        self.loginBtn.config(bg="#333",fg='white', bd=1, relief='raised', font=('Verdana', 10,'bold'))
        self.loginBtn.grid_configure(ipady=7, pady=25, ipadx=30)

        self.signupLink = Label(frame, text="THIS IS A ONE TIME LOGIN")
        self.signupLink.grid(row=4, column=0, sticky='nsew')
        self.signupLink.config(bg='#FFFFFF', fg='#333' , font=('Verdana', 10,'bold'))
        self.signupLink.grid_configure(ipady=7, pady=15, ipadx=30)

    
    def login(self):
        #remove this LoginGui and show the next interface
        if len(self.emailEntry.get()) > 1:
           self.label.config(text="Login Successful!")
           self.pack_forget()
           MainGui(self.master)
        else:
             self.validEmailText.config(text='please enter your email',fg='red')

window = Tk()
if __name__ == '__main__':
    window.title("ChatApp")
    container = Frame(window)
    container.pack(side='top', fill='both', expand='yes')
    LoginGui(container)
    window.mainloop()


