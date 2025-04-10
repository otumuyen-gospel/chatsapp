import tkinter as tk
import socket
import threading
import json

window = tk.Tk()
window.title("Server")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Connect", command=lambda : start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(topFrame, text="Stop", command=lambda : stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text = "Host: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text = "Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="**********Client List**********").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=15, width=30)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7", highlightbackground="grey", state="disabled")
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))


server = None
HOST_ADDR = "0.0.0.0"
HOST_PORT = 8080
client_name = " "
clients = []
clients_names = []
pending_msg = []                            #messages that are yet to be delivered


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT # code is fine without this
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_clients, (server,))

    lblHost["text"] = "Host: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)


# Stop server function
def stop_server():
    for client in clients:
        client.close()

    clients.clear()
    server.close()
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)
    window.quit()


def accept_clients(the_server):
    while True:
        client, addr = the_server.accept()
        clients.append(client)

        # use a thread so as not to block the gui thread
        threading._start_new_thread(send_receive_client_message, (client, addr))

def get_pending_messages(msg_list, client_name):
    for msg in pending_msg:
        if msg['recipient'] == client_name:
            msg['sent'] = True
            msg_list.append(msg)
    
    return msg_list


def clean_pending_messages():
    for msg in pending_msg:
        if msg['sent']:
            pending_msg.remove(msg)
    

# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    msg_list = []
    # send welcome message to client
    client_name  = json.loads(client_connection.recv(4096))['sender'] 
    msg = "welcome "+client_name + " type 'exit' to exit the the app"
    welcome_msg = {"sender":"SERVER", "recipient":client_name,"message":msg, "sent":True}

    msg_list.append(welcome_msg)
    msg_list = get_pending_messages(msg_list=msg_list, client_name=client_name)      
    #send both pending and welcome msg for this client 
    client_connection.send(bytes(json.dumps(msg_list), encoding="utf-8"))

    clean_pending_messages()                             #delete pending msgs delivered

    clients_names.append(client_name)

    update_client_names_display(clients_names)  # update client names display

    while True:
        data = json.loads(client_connection.recv(4096))
        if not data: break
        if data['message'] == "exit": break

        for name in clients_names:
            if name == data['recipient']:                             #recipient is online
                recipientIndex = clients_names.index(name)
                recipientConn = clients[recipientIndex]
                data['sent'] = True
                recipientConn.send(bytes(json.dumps(data), encoding="utf-8"))
                break

        if not data['sent']:                                         #not delivered save for later
            pending_msg.append(data)   
            

    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    server_msg = {"sender":"SERVER", "recipient":client_name,"message":"BYE", "sent":True}
    client_connection.send(bytes(json.dumps(server_msg), encoding="utf-8"))
    client_connection.close()

    update_client_names_display(clients_names)  # update client names display


# Return the index of the current client in the list of clients
def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


# Update client name display when a new client connects OR
# When a connected client disconnects
def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, c+"\n")
    tkDisplay.config(state=tk.DISABLED)


window.mainloop()
