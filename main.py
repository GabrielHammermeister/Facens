import re

T_KEYWORD = "keyword"
T_OP = "op"
T_INT = "int"
T_STRING = "string"
T_ID = "id"
T_EOF = "eof"

class Token():
    def _init_(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor

    def _str_(self):
        return '<%s %s>' % (self.tipo, self.valor)

class StopExecution(Exception):
    def render_traceback(self):
        pass

def afd_int(token):
    try:
        token = int(token)
        return True
    except:
        return False

def afd_string(token):
    if token[0] == '.' and token[-1] == '.':
        return True
    return False

def afd_identificador(token):
    if token in ["se", "enquanto"]:
        raise ValueError(f"'{token}' é uma palavra-chave e não pode ser usada como identificador.")

    regex = re.compile('[a-zA-Z0-9_]+')
    r = regex.match(token)
    if r is not None:
        if r.group() == token:
            return True
        else:
            return False
    else:
        return False

def afd_principal(token):
    if token == "init":
        return Token(T_KEYWORD, 'init')

    elif token == "se":
        return Token(T_KEYWORD, 'se')

    elif token == "enquanto":
        return Token(T_KEYWORD, 'enquanto')

    elif token == "imp":
        return Token(T_KEYWORD, 'imp')

    elif token in "=+-*":
        return Token(T_OP, token)

    elif token.startswith('.') and token.endswith('.'):
        return Token(T_STRING, token[1:-1])

    elif afd_int(token):
        return Token(T_INT, token)

    elif afd_identificador(token):
        return Token(T_ID, token)

    elif token in ["=", "+", "-", "*", ":", "?", ">", "<", ">=", "<=", "==", "!="]:
        return Token(T_OP, token)

    else:
        raise ValueError(f'Valor inesperado: "{token}"')

class Parser():
    def _init_(self, tokens, linha_atual=None):
        self.tokens = tokens
        self.pos = -1
        self.token_atual = None
        self.linha_atual = linha_atual
        self.proximo()

    def proximo(self):
        self.pos += 1
        if self.pos >= len(self.tokens):
            self.token_atual = Token(T_EOF)
        else:
            self.token_atual = self.tokens[self.pos]
        print(self.token_atual)
        return self.token_atual

    def erro(self):
        raise Exception(f'Erro de sintaxe na linha {self.linha_atual}.')

    def use(self, tipo, valor=None):
        if self.token_atual.tipo != tipo:
            self.erro()
        elif valor is not None and self.token_atual.valor != valor:
            self.erro()
        else:
            self.proximo()

    def statement(self):
        if self.token_atual.tipo == T_KEYWORD and self.token_atual.valor == "se":
            self.se_statement()
        elif self.token_atual.tipo == T_KEYWORD and self.token_atual.valor == "enquanto":
            self.enquanto_statement()
        elif self.token_atual.tipo == T_KEYWORD and self.token_atual.valor == "imp":
            self.imp_statement()
        elif self.token_atual.tipo == T_ID:
            self.atribuicao_statement()
        else:
            self.erro()

    def imp_statement(self):
        self.use(T_KEYWORD, valor="imp")
        self.use(T_STRING)

    def se_statement(self):
        self.use(T_KEYWORD, valor="se")
        self.expr()
        self.statement()

    def enquanto_statement(self):
        self.use(T_KEYWORD, valor="enquanto")
        self.expr()
        self.statement()

    def atribuicao_statement(self):
        self.use(T_ID)
        self.use(T_OP, valor="=")
        self.expr()

    def relacional_expr(self):
        """
        relacional_expr ::= <expr> <op_relacional> <expr>
        """
        self.expr()
        if self.token_atual.valor in [">", "<", ">=", "<=", "==", "!="]:
            self.use(T_OP)
            self.expr()

    def expr(self):
        if self.token_atual.tipo == T_INT or self.token_atual.tipo == T_ID:
            self.term()
            while self.token_atual.tipo == T_OP and self.token_atual.valor in ['+','-']:
                self.use(T_OP)
                self.term()
            if self.token_atual.tipo == T_OP and self.token_atual.valor in [">", "<", ">=", "<=", "==", "!="]:
                self.relacional_expr()
            if self.token_atual.tipo == T_OP and self.token_atual.valor == '?':
                self.ternario_expr()
        else:
            self.ternario_expr()

    def term(self):
        if self.token_atual.tipo == T_INT:
            self.use(T_INT)
        elif self.token_atual.tipo == T_ID:
            self.use(T_ID)
        else:
            self.erro()

def tokenize_line(line):
    tokens = []
    in_string = False
    buffer = []
    for word in line.split():
        if word.startswith('.') and not in_string:
            in_string = True
            buffer.append(word)
        elif word.endswith('.') and in_string:
            in_string = False
            buffer.append(word)
            tokens.append(' '.join(buffer))
            buffer.clear()
        elif in_string:
            buffer.append(word)
        else:
            tokens.append(word)
    return tokens



def main():
    arquivo = open('./test/codigo.x', 'r')
    ln = 1

    tokens = []

    for l in arquivo.readlines():
        l = l.replace('\n', '')
        for token in tokenize_line(l):
            try:
                tokens.append(afd_principal(token))
            except Exception as e:
                print(tokens)
                print(str(e) + " na posição %i da linha %i" % (l.index(token), ln))
                raise StopExecution
        ln += 1

    print([str(t) for t in tokens])

    parser = Parser(tokens, ln)
    parser.statement()
if __name__ == "__main__":
    main()