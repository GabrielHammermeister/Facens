/*

Gabriel Hammermeister M. da Costa   190162
Leonardo Muhamed Batista            190448
Enrico Reis Conto                   190793
*/

#include <stdio.h>

#define SUCCESS 0
#define FAIL 1
#define REPEAT 2
#define POOL_SIZE 10

typedef void (*Processo)();

typedef struct {
    Processo processo;
    int repeat;
} buffer_circular;

buffer_circular pool[POOL_SIZE];

int tail = 0;
int head = 0;

void inicializarBuffer() {
    for (int i = 0; i < POOL_SIZE; i++) {
        pool[i].processo = NULL;
        pool[i].repeat = 0;
    }
    printf("Inicialização do buffer concluída.\n\n");
}

int filaCheia() {
    return (tail + 1) % POOL_SIZE == head;
}

int vazia() {
    return head == tail;
}

char kernelAddProc(Processo nProcesso) {
    // Verifica se há espaço livre
    if (((tail + 1) % POOL_SIZE) != head) {
        pool[tail].processo = nProcesso;
        pool[tail].repeat = 0;
        tail = (tail + 1) % POOL_SIZE;
        printf("Processo adicionado com sucesso. Início: %d, Fim: %d\n", head, tail);
        return SUCCESS;
    }
    return FAIL;
}

int removeProcesso() {
    if (vazia()) {
        printf("Fila vazia!!\n");
        return 0;
    }

    head = (head + 1) % POOL_SIZE; // Move o índice da cabeça para remover o elemento da fila

    return 1;
}

void executarBuffer() {
    if (!vazia()) {
        Processo processoAtual = pool[head].processo;
        printf("Executando processo...\n");
        processoAtual(); // Executa o processo
        if (pool[head].repeat) {
            // Processo deseja repetição, adiciona novamente ao buffer
            kernelAddProc(processoAtual);
        }
        removeProcesso(); // Remove o processo após execução
    } else {
        printf("Nenhum processo a ser executado.\n");
    }
}

void processoA() {
    printf("Processo A em execução.\n");
}

void processoB() {
    printf("Processo B em execução.\n");
}

void processoC() {
    printf("Processo C em execução.\n");
}

void kernelLoop() {
    while (1) {
        executarBuffer();
    }
}

void kernelInit() {
    // Inicialização do kernel, se necessário
}

int main() {
    inicializarBuffer();
    kernelAddProc(processoA);
    kernelAddProc(processoB);
    kernelAddProc(processoC);

    kernelLoop(); // Iniciar o loop de execução do kernel

    return 0;
}
