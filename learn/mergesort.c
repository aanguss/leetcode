#include <stdlib.h>
#include <stdio.h>
#define DEBUG 0

/**
 * @brief print an array between index values
 * @param left - left index edge to start printing
 * @param right - right index edge to stop printing
 * @return none
 */
void printArray(int arr[], int left, int right) {
    int arrSize = right - left;
    printf(".\n");
    for (int i = 0; i <= arrSize; i++) {
        printf("debug - arr[%d] = %d\n", i, arr[i]);
    }
}

/**
 * @brief swap two values in an array
 * @param x - value to swap with y
 * @param y - value to swap with x
 * @return none
 */
void swap(int * x, int * y) {
    *x = *x ^ *y;
    *y = *x ^ *y;
    *x = *x ^ *y;
}

/**
 * @brief merge array in ascending order
 * @param arr - array to sort
 * @param left - left index of array to sort
 * @param middle - middle index of array to sort
 * @param right - right index of array to sort
 */
// void merge(int arr[], int left, int middle, int right) {
//     int leftSize = middle - left;
//     int rightSize = right - middle;
//     int totalSize = right - left;
//     int sortedArray[totalSize];
//     int i = left, j = middle, k = 0;

//     if(DEBUG) { printf("--debug start of merge from %d to %d--\n", left, right); }
//     printArray(arr, left, right);

//     while (i < middle && j <= right) {
//         if (arr[i] <= arr[j]) {
//             sortedArray[k] = arr[i];
//             if(DEBUG) { printf("arr_i[%d]=%d < arr_j[%d]=%d, k[%d]=%d\n", i, arr[i], j, arr[j], k, sortedArray[k]);
//             i++;
//         } else if (arr[i] > arr[j]) {
//             sortedArray[k] = arr[j];
//             if(DEBUG) { printf("arr_i[%d]=%d > arr_j[%d]=%d, k[%d]=%d\n", i, arr[i], j, arr[j], k, sortedArray[k]); }
//             j++;
//         } else {
//             printf("ERROR found...");
//             if(DEBUG) { return -1; }
//         }
//         k++;
//     }

//     if(DEBUG) { printf("done in while, i=%d, j=%d\n", i, j); }

//     while (i < middle) {
//         sortedArray[k] = arr[i];
//         if(DEBUG) { printf("arr_i[%d]=%d, k[%d]=%d\n", i, arr[i], k, sortedArray[k]); }
//         i++;
//         k++;
//     }

//     while (j <= right) {
//         sortedArray[k] = arr[j];
//         if(DEBUG) { printf("arr_j[%d]=%d, k[%d]=%d\n", j, arr[j], k, sortedArray[k]); }
//         j++;
//         k++;
//     }

//     i = left;
//     for (k = 0; k <= totalSize; k++) {
//         arr[i] = sortedArray[k];
//         if(DEBUG) { printf("deubg-after-party - arr[%d] = %d\n", k, arr[k]); }
//         i++;
//     }
// }

void merge(int arr[], int left, int middle, int right) {
    int leftSize = middle - left + 1;
    int rightSize = right - middle;
    int totalSize = right - left;
    int sortedArray[totalSize];
    int i = 0, j = 0, k = left;
    int leftArray[leftSize];
    int rightArray[rightSize];

    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < leftSize; i++) 
        leftArray[i] = arr[left + i]; 
    for (j = 0; j < rightSize; j++) 
        rightArray[j] = arr[middle + 1 + j]; 

    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray 
    j = 0; // Initial index of second subarray 
    k = left; // Initial index of merged subarray 
    while (i < leftSize && j < rightSize) 
    { 
        if (leftArray[i] <= rightArray[j]) 
        { 
            arr[k] = leftArray[i]; 
            i++; 
        } 
        else
        { 
            arr[k] = rightArray[j]; 
            j++; 
        } 
        k++; 
    } 
  
    /* Copy the remaining elements of L[], if there 
       are any */
    while (i < leftSize) 
    { 
        arr[k] = leftArray[i]; 
        i++; 
        k++; 
    } 
    /* Copy the remaining elements of R[], if there 
       are any */
    while (j < rightSize) 
    { 
        arr[k] = rightArray[j]; 
        j++; 
        k++; 
    }  
}

/**
 * @brief merge sort algorithm
 * @param arr - array pointer to be sorted
 * @param left - left index starting point to sort
 * @param right - right index ending point to sort
 * @return merged array
 */
// void mergeSort(int * arr, int left, int right) {
void mergeSort(int arr[], int left, int right) {
    int middle;

    if (left < right) {
        // find middle value
        middle = (left+right)/2;
        // split and recursively merge left side
        mergeSort(arr, left, middle);
        // split and recursively merge left side
        mergeSort(arr, middle + 1, right);
        // merge final arrays
        merge(arr, left, middle, right);
    }
}

// #define RAND_MAX = 1000;

int main(void) {
    // int arr[4] = {4, 3, 1, 0};
    // int arrSize = sizeof(arr)/sizeof(int);

    // int arr[7] = {38, 27, 43, 3, 9, 82, 10};
    // int arrSize = sizeof(arr)/sizeof(arr[0]);

    int arr[0x8000];

    for (int i = 0; i < 0x8000; i++) {
        arr[i] = rand();
    }

    int arrSize = sizeof(arr)/sizeof(arr[0]);

    // mergeSort(&arr[0], 0, arrSize-1);
    mergeSort(arr, 0, arrSize-1);

    // printf("--final array--\n");
    // for (int i = 0; i < arrSize; i++) {
    //     printf("arr[%d] = %d\n", i, arr[i]);
    // }
}