# request_handler.py

import os
import mimetypes


def get_content_type(file_path):
    return mimetypes.guess_type(file_path)[0] or 'application/octet-stream'


def handle_request(client_socket, base_dir):
    request_data = client_socket.recv(1024).decode('utf-8')
    # if not request_data:
    #     client_socket.close()
    #     print('no request data')
    #     return

    # if method != 'GET':
    #     response = "HTTP/1.1 501 Not Implemented\r\n\r\nMethod not implemented."
    #     client_socket.send(response.encode())
    #     client_socket.close()
    #     print('method not GET')
    #     return
    current_directory = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(current_directory, base_dir)
    print(file_path)
    # valida se o caminho eh valido ou se existe algum arquivo
    # if not os.path.exists(file_path) or not os.path.isfile(file_path):
    #     response = "HTTP/1.1 404 Not Found\r\n\r\nFile not found."
    #     client_socket.send(response.encode())
    #     client_socket.close()
    #     return

    with open('.' + base_dir, 'rb') as file:
        content = file.read()
        print(content)

    content_type = get_content_type(file_path)
    response_headers = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n"
    # Envie o cabeçalho de resposta
    client_socket.sendall(response_headers.encode())

    # Envie o conteúdo do arquivo (que já é bytes)
    client_socket.sendall(content)

    client_socket.close()