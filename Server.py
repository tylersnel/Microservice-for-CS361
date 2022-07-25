import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
#List where you can put URLs to send to client
da_list=[]
index_pos=0
while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received {message}")



    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string(da_list[index_pos])
    index_pos+=1

