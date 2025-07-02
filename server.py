import threading
import socket

host = 'localhost'
port = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Server started on {host}:{port}")

client_sockets = []
nicknames = []

def broadcast(message):
    for client in client_sockets:
        try:
            client.send(message)
        except Exception as e:
            print(f"Error sending message: {e}")
        
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message)
        except:
            index = client_sockets.index(client_socket)            
            client_sockets.remove(client_socket)            
            client_socket.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat.".encode('utf-8'))
            nicknames.remove(nickname)
            break
            
def accept_connections():
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established.")
        
        client_socket.send("NICK".encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        client_sockets.append(client_socket)
        
        print(f"Nickname of the client is {nickname.upper()}.")
        broadcast(f"{nickname} has joined the chat.".encode('utf-8'))
        
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

    
print("Server is running...")
accept_connections()