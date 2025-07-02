import threading
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICK':
                client_socket.send(input("Choose a nickname: ").encode('utf-8'))
            else:
                print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            client_socket.close()
            break

def write_message():
    while True:
        message = input()        
        client_socket.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_message_thread = threading.Thread(target=write_message)
write_message_thread.start()