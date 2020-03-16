#include <stdlib.h>
#include <stdio.h>

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