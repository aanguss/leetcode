#include <stdlib.h>
#include <stdio.h>

void printVal(int val) {
    printf("printVal = %d\n", val);
}

int main(void) {
    int i = 0;
    int done = 0;

    // pre plus plus
    printf("---pre plus plus---\n");
    while (done < 1) {
        printf("i = %d, ", ++i);
        if (i == 5) {
            done++;
        }
    }
    printf("\n");
    i = 0;

    // post plus plus
    printf("---post plus plus---\n");
    while (done < 2) {
        printf("i = %d, ", i++);
        if (i == 5) {
            done++;
        }
    }
    printf("\n");
    i = 0;

    // pre function plus plus
    printf("---pre function plus plus---\n");
    printVal(++i);
    printf("val now %d\n", i);
    i = 0;

    // pre function plus plus
    printf("---pre plus plus---\n");
    printVal(i++);
    printf("val now %d\n", i);
    i = 0;

    return 0;
}