#include <stdlib.h>
#include <stdio.h>

int factorial(int num) {
    int returnNum = 1;
    
    if (num >= 1) {
        returnNum = num * factorial(num - 1);
    }
    return returnNum;
}

int main(void) {
    int num = 6;

    printf("factorial(%d) = %d\n", num, factorial(num));

    return 0;
}