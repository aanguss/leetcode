#include <stdlib.h>
#include <stdio.h>
#define DEBUG 0

int binarySearch(int * arr, int val, int low, int high) {
    int middleIndex = (high + low) / 2;
    int middleValue = arr[middleIndex];

    if (val == arr[middleIndex]) {
        return middleIndex;
    } else if (val < arr[low] || val > arr[high]) {
        printf("ERROR - value not found in array");
        return -1;
    } else {
        if (val <= arr[middleIndex]) {
            binarySearch(arr, val, low, middleIndex);
        } else if (val > arr[middleIndex]) { 
            binarySearch(arr, val, middleIndex + 1, high);
        }
    }
}

int main(void) {
    int index0, index1, index2;
    int arr[7] = {38, 27, 43, 3, 9, 82, 10};
    int arrSize = sizeof(arr)/sizeof(arr[0]);

    printf("--start array--\n");
    printFullArray(arr, arrSize);


    mergeSort(arr, 0, arrSize-1);

    printf("--sorted array--\n");
    printFullArray(arr, arrSize);
    
    printf("--binary search 43--\n");
    index0 = binarySearch(arr, 43, 0, arrSize - 1);
    printFullPivotArray(arr, arrSize, index0);
    
    printf("--binary search 0--\n");
    index1 = binarySearch(arr, 0, 0, arrSize - 1);
    printFullPivotArray(arr, arrSize, index1);

    printf("--binary search 100--\n");
    index2 = binarySearch(arr, 100, 0, arrSize - 1);
    printFullPivotArray(arr, arrSize, index2);
    // for (int i = 0; i < arrSize; i++) {
    //     printf("arr[%d] = %d\n", i, arr[i]);
    // }
}