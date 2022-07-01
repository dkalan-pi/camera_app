# echo-server.py

import socket
import time

HOST = "192.168.11.29"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # add the below line so the socket connection can be re-used (if not error will pop on s.bind((host,port)) statement)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with open('rcv.png','wb')as f:
        #print('file opened!')
        while True:
            # to handle 'connection reset by server' encounter at Client program
            try:
                data = conn.recv(1024)
            except:
                pass
            #print('data=%s' , (data))
            
            if  not data:
                break
            else:
                #time.sleep(2)
                f.write(data)
    f.close()
s.close()    
        