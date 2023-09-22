
/*

Mateus da Silva do Prado - 190477
Felipe Lima Carvalho - 190190
Derik Caceres - 190695
João Victor Timo - 190826

*/


#include <stdio.h>

//#define TAMANHO_BUFFER 6
#define SUCCESS 0
#define FAIL 1
#define REPEAT 2
#define POOL_SIZE 10

typedef void (*Processo)();

typedef struct {
    Processo processo;
} buffer_circular;

buffer_circular pool[POOL_SIZE];

int tail = 0;
int head = 0;

void inicializarBuffer() {
    for (int i = 0; i < POOL_SIZE; i++) {
        pool[i].processo = NULL;
    }
    printf("Processo de inialização do buffer finalizado\n\n");
}

int filaCheia(){
    return (tail + 1) % POOL_SIZE == head;
}

char kernelAddProc(Processo* nProcesso) {
    //Verifica de há espaço livre
    if (((tail + 1) % POOL_SIZE) != head) {
        pool[tail].processo = nProcesso;
        tail = (tail + 1) % POOL_SIZE;
        printf("Inicio: %d, Fim: %d\n", head, tail);
        return SUCCESS;
    }
    return FAIL;
}

int vazia(){
	return (head == tail );
}

int removeProcesso(){
    
	if(vazia()){
		printf("Fila vazia!!\n");
		return 0;
	}
	
	pool[head++]; // remove o elemento da fila
	
	if(head == POOL_SIZE)
		head = 0;
		
	return 1;
}


void executarBuffer() {
    if (pool[head].processo != NULL) {
        pool[head].processo();
        removeProcesso();
    }else{
        printf("Função no índice %d é nula!\n", head);
    } 
}


void funcao1() {
    printf("Função 1\n");
}

void funcao2() {
    printf("Função 2\n");
}

void funcao3() {
    printf("Função 3\n");
}

void funcao4() {
    printf("Função 4\n");
}


void funcao5() {
    printf("Função 5\n");
}

void kernelLoop() {
    while(1) {
        for(int i = 0 ; i < POOL_SIZE ; i++) {
            executarBuffer();

        }
    }
    // refinar
}
void kernelInit() {
    // completar
}


int main() {
    inicializarBuffer();
    kernelAddProc(&funcao1);
    kernelAddProc(&funcao2);

    kernelAddProc(&funcao3);

    kernelAddProc(&funcao4);

    executarBuffer();

    return 0;
}