from tkinter import *
class MainGui(Frame):
    MSG_TYPE =["outgoing", "incoming",'outfile', 'infile']
    def __init__(self, master = None):
        super().__init__(master)
        self.createGui()
    def createGui(self):
        self.pack(side='top', fill='both', expand='yes')
        self.config(bg='white')
        self.statusBar()
        self.MenusBar()
        self.chatMsg()
        self.sendBar()
    def statusBar(self):
        frame = Frame(self)
        frame.pack(side=TOP, expand=YES, fill=X, anchor=N)
        frame.config(bg='purple')
        self.name = Label(frame, text='Otumuyengospel@gmail.com')
        self.name.config(background='purple',fg='white', font=('verdana',15,'bold'))
        self.name.pack(side=TOP, fill=BOTH, expand=YES, anchor=N)
        self.status = Label(frame, text='Offline')
        self.status.config(background='purple',fg='white', font=('verdana',8,'bold'))
        self.status.pack(side=BOTTOM, fill=BOTH, expand=YES, anchor=S)
    def MenusBar(self):
        menus = ['Settings', 'Contacts', 'Groups']
        frame = Frame(self)
        frame.pack(side=LEFT, expand=YES, fill=Y, anchor=N)
        frame.config(bg='#333')
        for i in range(len(menus)):
            menu = Button(frame, text=menus[i], command=lambda m=menus[i]:self.selectMenu(m))
            menu.config(width=9,bg='#333', fg='white', font=('verdana',10,'bold'), bd=0, relief='raised')
            menu.grid(row=i,column=0, ipadx=90, ipady=10, padx=10, pady=10)
        
    def selectMenu(self, menu):
        if menu == "Settings":
            self.centerFrame.pack_forget()
            self.settings()
        elif menu == "Contacts":
            self.centerFrame.pack_forget()
            self.contacts()
        elif menu == "Groups":
            self.centerFrame.pack_forget()
            self.groups()
        else:
             self.centerFrame.pack_forget()
             self.chatMsg()
    def settings(self):
        self.centerFrame = Frame(self)
        self.centerFrame.pack(side=TOP, expand=YES, fill=BOTH, anchor=N)
        self.centerFrame.config(bg='white')
    def contacts(self):
        self.centerFrame = Frame(self)
        self.centerFrame.pack(side=TOP, expand=YES, fill=BOTH, anchor=N)
        self.centerFrame.config(bg='white')
    def groups(self):
        self.centerFrame = Frame(self)
        self.centerFrame.pack(side=TOP, expand=YES, fill=BOTH, anchor=N)
        self.centerFrame.config(bg='white')
    def chatMsg(self):  
        self.centerFrame = Frame(self)
        self.centerFrame.pack(side=TOP, expand=YES, fill=BOTH, anchor=N)
        self.centerFrame.config(bg='white')
        scrollBar = Scrollbar(self.centerFrame)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.chats = Text(self.centerFrame, height=28, width=150)
        self.chats.pack(side=LEFT, fill=Y, padx=(5, 0))
        scrollBar.config(command=self.chats.yview)
        self.chats.config(yscrollcommand=scrollBar.set, background='white')
        self.chats.tag_config(tagName="outgoing",background="#333", foreground="white",
                              relief='raised',selectbackground='royalblue',justify="left",
                              lmargin1=50, rmargin=400, rmargincolor='white', lmargincolor='white', font=('verdana', 10,"bold"),
                              spacing1=2, wrap='word')
        self.chats.tag_config(tagName="incoming",background="purple", foreground="white",
                              relief='raised',selectbackground='royalblue',justify='right',
                               lmargin1=400, rmargin=50, rmargincolor='white', lmargincolor='white', font=('verdana', 10,"bold"),
                              spacing1=2, wrap='word')
        
        self.chats.insert(END, "\n")
        self.create_chat("Good Bye my guy", "6:00PM","Otumsgosepel@gmail.com",self.MSG_TYPE[1])
      
    def create_chat(self, msg, time, sender, type):
       text = sender + "\n"+msg+"\n"+time+"\n"
       self.chats.insert(END, text, type)
       self.chats.insert(END, "\n\n")
       self.chats.see(END)
    def sendBar(self):   #for setting and sending messages
        frame = Frame(self)
        frame.config(bg='white')
        frame.pack(side=BOTTOM, expand=YES, fill=X, anchor=S)
        self.send = Button(frame, text='SEND', height=2, width=8)
        self.send.pack(side=LEFT)
        self.send.config(background="purple", fg='white', font=('verdana',10,'bold'))
        self.msg = Text(frame, height=1)
        self.msg.focus_set()
        self.msg.pack(side=LEFT, fill=BOTH, expand='yes')
        self.msg.config(background="white", bd=0,
                             highlightbackground="grey", font=('verdana',14,'normal')) 
        self.send.config(command=lambda:self.send_Message(msg=self.msg.get('1.0',END),
                                                         time='4:50PM',
                                                         sender="otumsgosepel@gmail.com",
                                                         type=self.MSG_TYPE[0])) 
    
    def send_Message(self, msg, time, sender, type):
        self.create_chat(msg=msg, time=time,sender=sender,type=type)
        self.msg.delete("1.0", END)