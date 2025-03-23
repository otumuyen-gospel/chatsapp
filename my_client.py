import tkinter as tk
from tkinter import messagebox
import socket
import threading
import json

window = tk.Tk()
window.title("Client")
message = {"sender":'', "recipient":'', "message":'', "sent":False}


topFrame = tk.Frame(window)
lblName = tk.Label(topFrame, text = "Name:").pack(side=tk.LEFT)
entName = tk.Entry(topFrame)
entName.pack(side=tk.LEFT)
lblRecipient = tk.Label(topFrame, text = "Recipient:").pack(side=tk.LEFT)
entRecipient = tk.Entry(topFrame)
entRecipient.pack(side=tk.LEFT)
btnConnect = tk.Button(topFrame, text="Connect", command=lambda : connect())
btnConnect.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP)

displayFrame = tk.Frame(window)
lblLine = tk.Label(displayFrame, text="*********************************************************************").pack()
scrollBar = tk.Scrollbar(displayFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=20, width=55)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
tkDisplay.tag_config("tag_your_message", foreground="blue")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
displayFrame.pack(side=tk.TOP)


bottomFrame = tk.Frame(window)
tkMessage = tk.Text(bottomFrame, height=2, width=55)
tkMessage.pack(side=tk.LEFT, padx=(5, 13), pady=(5, 10))
tkMessage.config(highlightbackground="grey", state="disabled")
tkMessage.bind("<Return>", (lambda event: getChatMessage(tkMessage.get("1.0", tk.END))))
bottomFrame.pack(side=tk.BOTTOM)


# network client
client = None
HOST_ADDR = "0.0.0.0"
HOST_PORT = 8080

def connect():
    if len(entName.get()) > 1:
        if len(entRecipient.get()) > 1:
            message["sender"] = entName.get()
            message["recipient"] = entRecipient.get()
            connect_to_server(message)
        else:
           tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your recipient name <e.g. John>")
    else:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your first name <e.g. John>")
        


def connect_to_server(msg):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(bytes(json.dumps(msg), encoding="utf-8")) # Send names to server after connecting

        entName.config(state=tk.DISABLED)
        btnConnect.config(state=tk.DISABLED)
        tkMessage.config(state=tk.NORMAL)

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive_message_from_server, (client,))
    except Exception as e:
        tk.messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(HOST_PORT) + " Server may be Unavailable. Try again later")


def receive_message_from_server(sck):
    while True:
        from_server = json.loads(sck.recv(1024))

        if not from_server: break

        # display message from server on the chat window

        # enable the display area and insert the text and then disable.
        # why? Apparently, tkinter does not allow us insert into a disabled Text widget :(
        texts = tkDisplay.get("1.0", tk.END).strip()
        tkDisplay.config(state=tk.NORMAL)
        if isinstance(from_server, list):
            for msg in from_server:
                server_msg = msg['sender'] +" -> "+msg['message']
                tkDisplay.insert(tk.END, server_msg + "\n\n")
        else:
            msg = from_server['sender'] +" -> "+from_server['message']
            if len(texts) < 1:
                tkDisplay.insert(tk.END, msg)
            else:
                tkDisplay.insert(tk.END, "\n\n"+ msg)

        tkDisplay.config(state=tk.DISABLED)
        tkDisplay.see(tk.END)

    sck.close()
    window.destroy()


def getChatMessage(msg):

    msg = msg.replace('\n', '')
    texts = tkDisplay.get("1.0", tk.END).strip()

    # enable the display area and insert the text and then disable.
    # why? Apparently, tkinter does not allow use insert into a disabled Text widget :(
    tkDisplay.config(state=tk.NORMAL)
    if len(texts) < 1:
        tkDisplay.insert(tk.END, "You -> " + msg, "tag_your_message") # no line
    else:
        tkDisplay.insert(tk.END, "\n\n" + "You -> " + msg, "tag_your_message")

    tkDisplay.config(state=tk.DISABLED)

    message["message"] = msg
    if len(entRecipient.get()) > 1:
        message["recipient"] = entRecipient.get()            #allows user to change recipient
        send_mssage_to_server(message)
    else:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your recipient name <e.g. John>")

    tkDisplay.see(tk.END)
    tkMessage.delete('1.0', tk.END)


def send_mssage_to_server(msg):
    client.send(bytes(json.dumps(msg), encoding="utf-8"))
    if msg['message'] == "exit":
        client.close()
        window.destroy()


window.mainloop()
