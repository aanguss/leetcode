#include <stdlib.h>
#include <stdio.h>

/**
 * @brief return fibonacci value for a given position using recursion
 * @param pos position to return value of
 * @return fib value for a given position
 */
int fibRe(int pos) {
    int lastOne;
    int lastTwo;

    if (pos < 0) {
        printf("ERROR - invalid position request");
        return 0;
    }

    if (pos == 0 || pos == 1) {
        return pos;
    } else {
        // printf("--->Start of fibRe(%d)\n", pos);
        lastOne = fibRe(pos - 1);
        // printf("--->lastOne = %d\n", lastOne);
        lastTwo = fibRe(pos - 2);
        // printf("--->lastTwo = %d\n", lastTwo);

        return (lastOne + lastTwo);
    }
}

/**
 * @brief return fibonacci value for a given position using
 * @param pos position to return value of
 * @return fib value for a given position
 */
int fib(int pos) {
    int fibVal[pos];
    fibVal[0] = 0;
    fibVal[1] = 1;

    if (pos < 0) {
        printf("ERROR - invalid position request");
        return -1;
    }

    if (pos == 0 || pos == 1) {
        return pos;
    } else {
        for (int i = 2; i <= pos; i++) {
            fibVal[i] = fibVal[i-1] + fibVal[i-2];
        }

        return fibVal[pos];
    }
}

/**
 * @brief driver support for testing fib(...)
 * @return 0 if no errors found
 */
int main(void) {
    int fibIndex0 = 0;
    int fibIndex1 = 2;
    int fibIndex2 = 5;
    
    printf("---Linear---\n");
    printf("fib(%d) = %d\n", fibIndex0, fib(fibIndex0));
    printf("fib(%d) = %d\n", fibIndex1, fib(fibIndex1));
    printf("fib(%d) = %d\n", fibIndex2, fib(fibIndex2));

    printf("---Recursion---\n");
    printf("fibRe(%d) = %d\n", fibIndex0, fibRe(fibIndex0));
    printf("fibRe(%d) = %d\n", fibIndex1, fibRe(fibIndex1));
    printf("fibRe(%d) = %d\n", fibIndex2, fibRe(fibIndex2));
}
