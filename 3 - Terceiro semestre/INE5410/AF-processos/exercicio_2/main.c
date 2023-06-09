#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>

//                          (principal)
//                               |
//              +----------------+--------------+
//              |                               |
//           filho_1                         filho_2
//              |                               |
//    +---------+-----------+          +--------+--------+
//    |         |           |          |        |        |
// neto_1_1  neto_1_2  neto_1_3     neto_2_1 neto_2_2 neto_2_3

// ~~~ printfs  ~~~
//      principal (ao finalizar): "Processo principal %d finalizado\n"
// filhos e netos (ao finalizar): "Processo %d finalizado\n"
//    filhos e netos (ao inciar): "Processo %d, filho de %d\n"

// Obs:
// - netos devem esperar 5 segundos antes de imprmir a mensagem de finalizado (e terminar)
// - pais devem esperar pelos seu descendentes diretos antes de terminar

int main(int argc, char** argv) {

    pid_t pidFilho = getpid();
    pid_t *ptrFilho;
    ptrFilho = &pidFilho;

    pid_t pidNeto = getpid();
    pid_t *ptrNeto;
    ptrNeto = &pidNeto;

    for (int i = 0; i < 2; i++) {
        if (pidFilho != 0) {                //Pai entra e cria dois filhos.
            printf("PID MAIN = %d\n", getpid());
            *ptrFilho = fork();
        }
    }

    if (pidFilho == 0) {                    //Filhos entram.
        printf("Processo %d, filho de %d\n", getpid(), getppid());
        
        for (int i = 0; i < 3; i++) {       //Criam três filhos cada.
            if (pidNeto != 0) {
                *ptrNeto = fork();
        }
    }

    if (pidNeto != 0) { 
        wait(NULL);
        printf("FILHOS: Processo %d finalizado\n", getpid());
    }

    if (pidNeto == 0) { 
        printf("Processo %d, filho de %d\n", getpid(), getppid());
        sleep(5);
        printf("NETOS: Processo %d finalizado\n", getpid());
    }

}
    // ....

    /*************************************************
     * Dicas:                                        *
     * 1. Leia as intruções antes do main().         *
     * 2. Faça os prints exatamente como solicitado. *
     * 3. Espere o término dos filhos                *
     *************************************************/
    
    if (pidFilho != 0) {
        wait(NULL);
       printf("Processo principal %d finalizado\n", getpid());     
    }

    return 0;
}
