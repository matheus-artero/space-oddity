from time import sleep
import socket
import os

host = os.environ["DB_HOST"]
port = int(os.environ["DB_PORT"])

print("Wait_for_it said: Esperando pelo container do banco de dados")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(30):
    try:
        s.connect((host, port))
        text = "Container do banco de dados pronto"
        break
    except socket.error as ex:
        sleep(1)
else:
    text = "Não pode se conectar ao container do banco de dados"

print(f"Wait_for_it said: {text}")
s.close()