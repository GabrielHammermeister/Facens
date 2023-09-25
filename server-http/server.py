# server.py

import socket
import os
import threading
from request_handler import handle_request

def main():
    # Configuração inicial
    host = '127.0.0.1'
    port = 8081
    # Verifique se a porta está em uso e encerre qualquer processo anterior
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.close()
    except OSError:
        print(f"A porta {port} está em uso. Encerrando processo anterior, se houver.")
        os.system(f"kill $(lsof -t -i:{port})")


    # Inicia o socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor HTTP rodando em http://{host}:{port}")

    # Loop para aceitar conexões
    while True:
        client_socket, client_addr = server_socket.accept()

        # Lê a URL da requisição HTTP
        request_data = client_socket.recv(1024).decode('utf-8')
        if not request_data:
            client_socket.close()
            continue

        request_lines = request_data.split('\n')
        request_line = request_lines[0]
        _, url, _ = request_line.strip().split()

        # Inicia uma nova thread para lidar com a conexão
        threading.Thread(target=handle_request(client_socket, url), args=(client_socket,)).start()

if __name__ == "__main__":
    main()
