import os
def clear_terminal(message):
    os.system('clear')
    print('----------------------------')
    print(message)

if 'TERM' not in os.environ:
    os.environ['TERM'] = 'xterm'
def response_200(status_code, content):
    message = f"Status Code: {status_code} \ncontent: {content}"
    clear_terminal(message)
    return message

def response_404():
    status_code = "404 Not Found"
    error_message = "Arquivo não encontrado."
    message = f"Status Code: {status_code} \nerror_message: {error_message}"
    clear_terminal(message)
    return message


def response_502():
    status_code = "502 Bad Gateway"
    error_message = "Função inválida."
    message = f"Status Code: {status_code} \nerror_message: {error_message}"
    clear_terminal(message)
    return message
