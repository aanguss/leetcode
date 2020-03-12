#include <stdlib.h>
#include <stdio.h>

void arraySum(int * arr, int val, int len, int * arrayOut) {
    // int lenOfArr = sizeof(arr)/sizeof(arr[0]);
    int * arrayReturn = malloc(sizeof(int) * len);
    int arrRetPos = 0;
    // int arrayReturn[lenOfArr][lenOfArr];

    // char ** blah = { "hah", "nah"};

    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len - 1; j++) {
            if (arr[i] + arr[j] == val) {
                arrayReturn[arrRetPos++] = i;
                arrayReturn[arrRetPos++] = j;
            }   
        }
    }

    // return arrayReturn;
}

int main(void) {
    int array[5] = {1, 2, 5, 4, 3};
    int len = sizeof(array)/sizeof(array[0]);
    int arrayOut[5];

    arraySum(array, 7, len, &arrayOut[0]);

    for (int i = 0; i < len; i++) {
        printf("%d\n", arrayOut[i]);
    }
    


    return 0;
}