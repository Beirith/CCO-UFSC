#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int min;
    int max;
}MinMax; 

void inputArray(int * arr, int size){
    for (int i = 0; i < size; i++) {
        scanf("\n%d", &arr[i]);
    }
    printf("\n");
}

void printArray(int * arr, int size){
    printf("\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int sortAscending(int * num1, int * num2){
    return *num1 - *num2;
}

int sortDescending(int * num1, int * num2){
    return *num2 - *num1;
}

void sort(int * arr, int size, int (* compare)(int *, int *)){
    int aux;

    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
        
            if (compare(&arr[i], &arr[j]) > 0) {
                aux = arr[i];
                arr[i] = arr[j];
                arr[j] = aux;
            }
        }
    }
}

int main(){
    int size;

    printf("Enter array size: ");
    scanf("%d", &size);

    int arr[size];

    printf("Enter elements in array: ");
    inputArray(arr, size);

    printf("\n\nElements before sorting: ");
    printArray(arr, size);

    printf("\n\nArray in ascending order: ");
    sort(arr, size, sortAscending);
    printArray(arr, size);

    printf("\nArray in descending order: ");
    sort(arr, size, sortDescending);
    printArray(arr, size);

    return 0;
}
