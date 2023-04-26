#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int min;
    int max;
}MinMax; 

MinMax *getMinMax(int * array, const int SIZE) {

    MinMax *result = (MinMax *)malloc(sizeof(MinMax));

    result->min = array[0];
    result->max = array[0];

    for (int i = 0; i < SIZE; i++) {

        if (array[i] > result->max) {
            result->max = array[i];
        }

        if (array[i] < result->min) {
            result->min = array[i];
        }
    }

    return result;
}

void main () {

    int vetor[10] = {5, -2, 9, 46, 88, -40, 0, 14, 70, 1};

    MinMax *a = getMinMax(vetor, 10);

    printf("max = %d, min = %d", a->max, a->min);
}