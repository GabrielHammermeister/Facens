# file_handler.py

def read_file(file_path):
    print(file_path)
    # valida se o caminho eh valido ou se existe algum arquivo
    # if not os.path.exists(file_path) or not os.path.isfile(file_path):
    #     response = "HTTP/1.1 404 Not Found\r\n\r\nFile not found."
    #     client_socket.send(response.encode())
    #     client_socket.close()
    #     return

    # Lê o conteúdo do arquivo
    with open('./' + file_path, 'rb') as file:
        content = file.read()
        print(content)
    return content
