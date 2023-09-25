# request_handler.py

import os
import mimetypes

import file_handler
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
    print("current_DIR: " + current_directory)
    # file_path = os.path.join(current_directory, base_dir)
    file_path = current_directory + base_dir
    print("file path: " + file_path)
    content = file_handler(file_path)

    content_type = get_content_type(file_path)
    response_headers = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n"
    # Envie o cabeçalho de resposta
    client_socket.sendall(response_headers.encode())

    # Envie o conteúdo do arquivo (que já é bytes)
    client_socket.sendall(content)

    client_socket.close()