import socket
import sys

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8899

    try:
        soc.connect((host, port))
    except:
        print("Erro na conexão")
        sys.exit()

    print("Digite '/sair' para sair")
    msg = input(" -> ")

    while msg != '/sair':
        soc.sendall(msg.encode("utf8"))

        data = soc.recv(5120).decode("utf8")

        print(data)

        msg = input(" -> ")

        data = ""

    soc.send(b'/sair')

if __name__ == "__main__":
	main()
