# echo-client.py

from multiprocessing.connection import wait
import socket
import time
from socket import error as SocketError
import errno

HOST = "192.168.11.29"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class client():
    def main1(file):
                
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # add the below line so the socket connection can be re-used (if not error will pop on s.bind((host,port)) statement)
            #Ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((HOST, PORT))
            ##conn, addr = s.accept()
            """ with conn:
                print(f"Connected by {addr}") """
            #filename = file
            f = open(file,'rb')
            l = f.read(1024)
            while(l):
                s.send(l)
                print('Sent',repr(l))
                l = f.read(1024)
                #time.sleep(3)
                #print('Done sending')
            exit()
                
