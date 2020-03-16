void swap(int * x, int * y) {
    *x = *x ^ *y;
    *y = *x ^ *y;
    *x = *x ^ *y;
}

int partition(int *arr, int low, int high) {
    int partIndex = low;

    for (int i = low; i <= high; i++) {

        if (arr[i] < arr[partIndex]) {
            swap(&arr[i], &arr[partIndex]);
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