# Microservice-for-CS361
A microservice for CS361 that sends strings to client

# How to REQUEST data:
1. MUST import Zeromq library. See https://zeromq.org/get-started/ on how to import.
2. Create and set variable context=zmq.Context()
3. Create and set variable socket = context.socket(zmq.REQ)
4. Connect to socket.connect("tcp://some_address")
5. Create a list to receive data
6. Create for loop in range for requests.
7. In for loop, send message to to socket. socket.send(b"message here")
8. Message must be 'low', 'medium', 'high' or 'perfect' else error message is sent

REQUEST EXAMPLE (Python):
```
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
da_list=[]

for request in range(1):
    print(f"Sending request {request} …")
    socket.send(b"message") 

```

# How to RECEIVE data:
1. Inside current for loop, create and assign variable message = socket.recv()
2. Since return message is a string, decode message by message=message.decode("utf-8")
3. Append message to list created earlier. da_list.append(message)

RECEIVE EXAMPLE (Python):
```
    message = socket.recv()
    print(f"Received {message} ")
    message=message.decode("utf-8")
    da_list.append(message)
```
    
# OVERALL EXAMPLE (Python):
```
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
da_list=[]

for request in range(1):
    print(f"Sending request {request} …")
    socket.send(b"message") 


    message = socket.recv()
    print(f"Received {message} ")
    message=message.decode("utf-8")
    da_list.append(message)
 ```
 
 # UML SEQUENCE DIAGRAM
 ![Capture](https://user-images.githubusercontent.com/67352917/180783774-a3a18e9c-d370-4f63-b0d5-1d69b7251f2d.JPG)
 
 # Installation:
 1. See https://zeromq.org/get-started/ on how to add library to IDE
 2. Download Server.py
 3. Run in seperate terminal in preferred IDE

 
