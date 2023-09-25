# file_handler.py
import os

# NAO CONSEGUIMOS RETORNAR O ARQUIVO INDEX.HTML PARA O CLIENTE
# DEVIDO A UM ERRO DE FORMATO INVALIDO

def read_file(file_path, client_socket):
    # valida se o arquivo e valido
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        response = "HTTP/1.1 404 Not Found\r\n\r\nFile not found."
        # client_socket.send(response.encode())
        print(f"Response: {response}")
        client_socket.close()
        return
    else:
        # lenco o conteudo do arquivo
        with open(file_path, 'rb') as file:
            return file.read()