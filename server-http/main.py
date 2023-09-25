# main.py
import server
import os

def read_and_print_index_html(base_dir):
    index_path = os.path.join(base_dir, 'index.html')

    if os.path.exists(index_path) and os.path.isfile(index_path):
        with open(index_path, 'r') as index_file:
            index_content = index_file.read()
            print(index_content)
    else:
        print("O arquivo index.html não foi encontrado no diretório base.")

# Exemplo de uso
base_dir = './'

if __name__ == "__main__":
    # read_and_print_index_html(base_dir)

    server.main()
