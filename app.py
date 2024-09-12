# app.py
import socket
from flask import Flask

app = Flask(__name__)

@socket.route('/')
def home():
    return "Hello from Docker!"

if __name__ == '__main__':
    socket.run(host='0.0.0.0', port=5000)
    if __name__ == '__main__':
    socket.run(host='0.0.0.0', port=5000) 