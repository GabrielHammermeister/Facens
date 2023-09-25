# http_responses.py

def response_200(status_code, content):
    print(f"Status Code: {status_code}")
    print(f"content: {content}")
    return f"Status Code: {status_code} \n\ncontent: {content}"
def response_404():
    status_code = "404 Not Found"
    error_message = "Arquivo não encontrado."
    print(f"Status Code: {status_code}")
    print(f"Error Message: {error_message}")
    return f"Status Code: {status_code} \n\nerror_message: {error_message}"


def response_502():
    status_code = "502 Bad Gateway"
    error_message = "Função inválida."
    print(f"Status Code: {status_code}")
    print(f"Error Message: {error_message}")
    return f"Status Code: {status_code} \n\nerror_message: {error_message}"
