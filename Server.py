
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
#List where you can put URLs to send to client
da_list=['https://i.imgur.com/6QvWi5Y.jpg',' https://i.imgur.com/T9egMZ1.jpg', 'https://i.imgur.com/ZilR5gd.jpg', 'https://i.imgur.com/aEiQMnX.jpg', 'Invalid message. Try again' ]
index_pos=0
while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received {message}")
    message = message.decode("utf-8")
    if message=='low':
        index_pos=0
    elif message=='medium':
        index_pos=1
    elif message=='high':
        index_pos=2
    elif message=='perfect':
        index_pos=3
    else:
        index_pos=4



    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string(da_list[index_pos])


