import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
da_list=[]

for request in range(3):
    print(f"Sending request {request} …")
    socket.send(b"Hello")



    #  Get the reply.
    message = socket.recv()
    print(f"Received {message} ")
    message=message.decode("utf-8")
    da_list.append(message)


print(da_list)



