// http://panthema.net/2013/sound-of-sorting/
// https://www.geeksforgeeks.org/quick-sort/

#include <stdio.h>
#include <stdlib.h>

void printArray(int * arr, int arrSize) {
    for (int i = 0; i < arrSize; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
}

void printPivotArray(int * arr, int low, int high, int pivot) {
    for (int i = low; i <= high; i++) {
        if (i == pivot) {
            printf("arr[%d] = %d<----\n", i, arr[i]);
        } else {
            printf("arr[%d] = %d\n", i, arr[i]);
        }
    }
}

void printSubArray(int * arr, int low, int high) {
    for (int i = low; i <= high; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
}
void swap(int * x, int * y) {
    *x = *x ^ *y;
    *y = *x ^ *y;
    *x = *x ^ *y;
}

int partition(int *arr, int low, int high) {
    int partIndex = low;

    // printf("..partition from %d to %d", low, high);

    for (int i = low; i <= high; i++) {

        if (arr[i] < arr[partIndex]) {
            // printf("found lower---------------\n");
            // printPivotArray(arr, low, high, partIndex);
            // printf("arr_i[%d]=%d, partIndex[%d]=%d\n", i, arr[i], partIndex, arr[partIndex]);
            swap(&arr[i], &arr[partIndex]);
            // printPivotArray(arr, low, high, partIndex);
        }
    }
    
    return partIndex;
}

void quickSort(int * arr, int low, int high) {
    int pivot;

    if (low < high) {
        pivot = partition(arr, low, high);

        quickSort(arr, low, pivot);
        quickSort(arr, pivot + 1, high);
    }
}

int main(void) {
    int arr[7] = {38, 27, 43, 3, 9, 82, 10};
    int arrSize = sizeof(arr)/sizeof(arr[0]);

    quickSort(arr, 0, arrSize-1);

    printf("--final array--\n");
    printArray(arr, arrSize);
}