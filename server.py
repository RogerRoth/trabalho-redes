import socket
import sys
import traceback
from threading import Thread
from datetime import date
import getmac
import platform
import requests

def main():
	start_server()


def start_server():
	host = "127.0.0.1"	# ip do server
	port = 8899		 # porta que o server esta escutando

	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # O sinalizador SO_REUSEADDR diz ao kernel para reutilizar um soquete local no estado TIME_WAIT, sem esperar que seu tempo limite natural expire
	print("Socket criado")

	try:
		soc.bind((host, port))
	except:
		print("Bind fallou! Error: " + str(sys.exc_info()))
		sys.exit()

	soc.listen(5)	   # porta aceita ate 5 conexões
	print("Socket agora esta operando")

	# loop infinito
	while True:
		conexao, addr = soc.accept()
		ip, port = str(addr[0]), str(addr[1])
		print("Conectado com " + ip + ":" + port)

		try:
			Thread(target=client_thread, args=(conexao, ip, port, host)).start()
		except:
			print("Erro na inicialização Thread.")
			traceback.print_exc()

	soc.close()

def client_thread(conexao, ip, port, host, tam_max_buffer = 1024):
	ativo = True

	while ativo:
		dados_cliente = receive_input(conexao, tam_max_buffer)

		if dados_cliente == "/QUEM":
			print ("Enviando para " + ip + " nome do server: Servidor Estudo")
			msg = "Nome do server: Servidor Estudo"
			conexao.sendto(msg.encode('utf-8'), (ip, int(port)))

		elif dados_cliente == "/DATA": #Retorna a data do sistema do Server
			data_server = date.today()
			dia = data_server.strftime('%d/%m/%Y')
			print ("Enviando para " + ip + " data do sistema do Server: " + dia)
			msg = 'Data do sistema do Server: ' + dia
			conexao.sendto(msg.encode('utf-8'), (ip, int(port)))

		elif dados_cliente == "/IP": #Retorna o IP do Server
			print ("Enviando para " + ip + " IP do Server: " + host)
			msg = "IP do Server: " + host
			conexao.sendto(msg.encode('utf-8'), (ip, int(port)))

		elif dados_cliente == "/MAC": #Retorna a MAC Address do Server
			mac_addr = getmac.get_mac_address()
			print ("Enviando para " + ip + " o MAC Address do Server: " + mac_addr)
			msg = "MAC Address do Server: " + mac_addr
			conexao.sendto(msg.encode('utf-8'), (ip, int(port)))

		elif dados_cliente == "/SYS": #Retorna Descrição do S.O. do Server
			info = "SO: "+ platform.system() +" | Maquina: "+platform.machine()+" | Rede: "+platform.node()+" | Plataforma: "+platform.platform()
			print ("Enviando para " + ip + " o Info do Server: "+ info)
			conexao.sendto(info.encode('utf-8'), (ip, int(port)))

		elif dados_cliente == "/DEV": #Retorna o nome do grupo
			grupo = "Grupo: Roger Rothmund | Yan Reckziegel Rodrigues"
			print ("Enviando para " + ip + " nome do grupo: "+ grupo)
			conexao.sendto(grupo.encode('utf-8'), (ip, int(port)))

		elif dados_cliente == "/DOLAR": #Retorna a cotação do dólar
			response = requests.get("https://dolarhoje.com/")
			txt = response.text
			div = txt.split("div")
			vl = div[3].split("\"")

			print ("Enviando para " + ip + " cotação do dólar: R$"+ vl[23])
			msg = "Cotação do dólar: R$"+ vl[23]
			conexao.sendto(msg.encode('utf-8'), (ip, int(port)))

		elif dados_cliente == "/TRENDS": #Retorna a cotação do dólar
			response = requests.get("https://trends24.in/")
			txt = response.text
			div = txt.split("trend-card__list")
			topic = div[1].split("<li title=")
			linha = topic[0].split("</a>")
			trends = ""
			for x in range (10):
				hashtag = linha[x].split("\">")
				index = x + 1
				trends = trends + str(index) + " - " + hashtag[1] + "\n" 

			print ("Enviando para " + ip + " trend topics do twitter: " + trends)
			conexao.sendto(trends.encode('utf-8'), (ip, int(port)))

		elif "/SAIR" in dados_cliente:
			print("Cliente requisitou a desconexão.")
			conexao.close()
			print("Conexão com " + ip + ":" + port + " encerrada.")
			ativo = False
		else:
			print("Comando invalido de: {}".format(dados_cliente))
			conexao.sendall("Comando Invalido!".encode("utf8"))


def receive_input(conexao, tam_max_buffer):
	dados_cliente = conexao.recv(tam_max_buffer)
	dados_cliente_size = sys.getsizeof(dados_cliente)

	if dados_cliente_size > tam_max_buffer:
		print("O tamanho dos dados recebidos é maior que o esperado {}".format(dados_cliente_size))

	decoded_entrada = dados_cliente.decode("utf8").rstrip()  # decodifica e retirar o final da linha
	res = process_input(decoded_entrada)

	return res


def process_input(entrada_str):	#Processa dados de entrada, altera tudo para maiuscula
	print("Processando os dados recebidos do cliente...")

	return str(entrada_str).upper()

if __name__ == "__main__":
	main()
