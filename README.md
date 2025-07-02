# TCP Chat Room

A simple multi-client chat room application using Python sockets and threading.

## Features

- Multiple clients can join and chat in real-time.
- Each client chooses a nickname.
- Server broadcasts messages to all connected clients.
- Notifies when users join or leave.

## Usage

### 1. Start the Server

Open a terminal and run:

```bash
python server.py
```

### 2. Start Clients

Open one or more terminals and run for each client:

```bash
python client.py
```

Each client will be prompted to enter a nickname.

### 3. Chat

- Type messages in any client window and press Enter to send.
- All connected clients will see the messages.

## Files

- `server.py`: The chat server.
- `client.py`: The chat client.
- `README.md`: This documentation.

## Notes

- The server listens on `localhost:8080` by default.
- To stop the server, press `Ctrl+C` in the server terminal.
- To exit a client, close its terminal window.
