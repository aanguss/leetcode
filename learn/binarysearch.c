#include <stdlib.h>
#include <stdio.h>
#define DEBUG 0

/**
 * @brief print entire array given
 * @param arr - array to print
 * @param arrSize - size of array to print
 */
void printFullArray(int * arr, int arrSize) {
    for (int i = 0; i < arrSize; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
}

void printFullPivotArray(int * arr, int arrSize, int pivot) {
    for (int i = 0; i < arrSize; i++) {
        if (i == pivot) {
            printf("arr[%d] = %d<----\n", i, arr[i]);
        } else {
            printf("arr[%d] = %d\n", i, arr[i]);
        }
    }
}

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