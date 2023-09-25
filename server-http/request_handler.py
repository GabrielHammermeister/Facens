# request_handler.py

import os
import mimetypes

import file_handler
import http_responses
def get_content_type(file_path):
    return mimetypes.guess_type(file_path)[0] or 'application/octet-stream'

def parse_request(request_data):
    # Divide as linhas da requisição
    request_lines = request_data.split('\n')

    # Extrai a linha de solicitação (primeira linha)
    request_line = request_lines[0].strip()

    # Divide a linha de solicitação em método, URL e versão HTTP
    method, url, http_version = request_line.split()

    # Extrai os cabeçalhos da requisição (pode haver vários)
    headers = {}
    for line in request_lines[1:]:
        if line.strip():
            header_name, header_value = line.strip().split(':', 1)
            headers[header_name.strip()] = header_value.strip()

    # Extrai o corpo da requisição (não tratado neste exemplo)
    body = None

    # Retorna um objeto de requisição com os componentes extraídos
    request = {
        "method": method,
        "url": url,
        "http_version": http_version,
        "headers": headers,
        "body": body
    }

    return request



def handle_request(client_socket, method, url):

    # print("PASSOU PRA CA4s")
    mapped_urls = ['/index.html', 'text.html']

    # request_data = client_socket.recv(1024).decode('utf-8')
    # request_lines = request_data.split('\n')
    # request_line = request_lines[0]
    # method, url, _ = request_line.strip().split()

    # print("PASSOU PRA CA3")
    if url not in mapped_urls:
        response = http_responses.response_404()
        client_socket.send(response.encode())
        client_socket.close()
        return

    # print("PASSOU PRA CA2")
    if method != 'GET':
        response = http_responses.response_502()
        client_socket.send(response.encode())
        client_socket.close()
        return
    # content = file_handler.read_file('.' + base_dir, client_socket)

    # Gera a resposta HTTP com base nos resultados da função handle_request
    # print("PASSOU PRA CA")
    response = http_responses.response_200(status_code="200 OK", content=f"{url}")
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()