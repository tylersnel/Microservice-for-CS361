# Microservice-for-CS361
A microservice for CS361 that sends strings to client

# How to REQUEST data:
1. MUST import Zeromq library. See https://zeromq.org/get-started/ on how to import.
2. Create and set variable context=zmq.Context()
3. Create and set variable socket = context.socket(zmq.REQ)
4. Connect to socket. soecket.connect("tcp://some_address")
5. Create a list to receive data
6. Create for loop in range for requests.
7. In for loop, send message to to socket. socket.send(b"message here")

REQUEST EXAMPLE (Python):
```import zmq

context = zmq.Context()


print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
da_list=[]

for request in range(3):
    print(f"Sending request {request} …")
    socket.send(b"Hello")```

# How to RECEIVE data:
1. Inside current for loop, create and assign variable message = socket.recv()
2. Since return message is a string, decode message by message=message.decode("utf-8")
3. Append message to list created earlier. da_list.append(message)

RECEIVE EXAMPLE (Python):
    message = socket.recv()
    print(f"Received {message} ")
    message=message.decode("utf-8")
    da_list.append(message)
    
# OVERALL EXAMPLE (Python):
 import zmq

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
da_list=[]

for request in range(3):
    print(f"Sending request {request} …")
    socket.send(b"Hello")


    message = socket.recv()
    print(f"Received {message} ")
    message=message.decode("utf-8")
    da_list.append(message)
 
 
