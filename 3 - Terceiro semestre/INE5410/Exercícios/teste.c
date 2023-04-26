#include <stdio.h>
#include <stdlib.h>

void mudaArray(int * vetor, int size) {

    for (int i =0; i < size; i++) {
        vetor[i] = i;
    }
}

void main () {

    int vetor[10] = {5, -2, 9, 46, 88, -40, -100, 14, 70, 1};
    int size = 10;

    for (int i = 0; i < size; i++) {
        printf("Array[%d] = %d\n", i, vetor[i]);
    }
}