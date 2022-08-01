
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
da_list=[]

for request in range(1):
    print(f"Sending request {request} …")
    socket.send(b"message") #message must be 'low', 'medium', 'high' or 'perfect' else error message is sent



    #  Get the reply.
    message = socket.recv()
    print(f"Received {message} ")
    message=message.decode("utf-8")
    da_list.append(message)



