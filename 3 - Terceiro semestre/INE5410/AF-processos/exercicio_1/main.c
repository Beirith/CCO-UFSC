#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>

//       (pai)      
//         |        
//    +----+----+
//    |         |   
// filho_1   filho_2


// ~~~ printfs  ~~~
// pai (ao criar filho): "Processo pai criou %d\n"
//    pai (ao terminar): "Processo pai finalizado!\n"
//  filhos (ao iniciar): "Processo filho %d criado\n"

// Obs:
// - pai deve esperar pelos filhos antes de terminar!


int main(int argc, char** argv) {

    pid_t pidFilho = getpid();
    pid_t *ptrPid;
    ptrPid = &pidFilho;

    for (int i = 0; i < 2; i++) {
        if (pidFilho != 0) {
            *ptrPid = fork();
        }
        if (pidFilho != 0) {
            printf("Processo pai criou %d\n", pidFilho);
        } 
    }
    if (pidFilho != 0) {
        wait(NULL);
        printf("Processo pai finalizado!\n"); 
    } else {
        printf("Processo filho %d criado\n", getpid());
    }
        
    /*************************************************
     * Dicas:                                        *
     * 1. Leia as intruções antes do main().         *
     * 2. Faça os prints exatamente como solicitado. *
     * 3. Espere o término dos filhos                *
     *************************************************/

    return 0;
}
