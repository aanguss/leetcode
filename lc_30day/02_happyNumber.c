/**
 * https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/
 * Happy Number
 * 
 * Write an algorithm to determine if a number n is "happy".
 * 
 * A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
 * 
 * Return True if n is a happy number, and False if not.
 * 
 * Example: 
 * 
 * Input: 19
 * Output: true
 * Explanation: 
 * 12 + 92 = 82
 * 82 + 22 = 68
 * 62 + 82 = 100
 * 12 + 02 + 02 = 1
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
// #include <math.h>

#define MAX_DIGITS 10
#define MAX_LOOPS 10000
int totalLoops = 0;

int power(int base, int exp) {
    int value = 1;

    for (int i = 0; i < exp; i++) {
        value *= base;
    }

    return value;
}

int getDigit(int num, int pos) {
    return 1;
}

bool isHappy(int n) {
    int digits[MAX_DIGITS];
    printf("\nNumber = %d\n", n);
    // int num = 1234;
    int currentDigit = 0;
    int currentRemain = 0;
    int numberOfDigits = 0;
    int totalValue = 0;

    // start recursive loops
    totalLoops++;

    for(int i = 1; i <= MAX_DIGITS; i++) {
        numberOfDigits++;
        currentRemain = n / power(10, i);
        currentDigit = (n % power(10,i)) / power(10, i - 1);

        // printf("currentRemain = %d, currentDigit = %d\n", currentRemain, currentDigit);
        if (currentRemain == 0 && currentDigit == 0) {
            numberOfDigits --;
            break;
        }
        // printf("%d.\t%d / %d = %d r%d\n", i, n, power(10,i), currentDigit, currentRemain);
        // printf("\tcurrentRemain = %d, currentDigit = %d\n", currentRemain, currentDigit);
        digits[i - 1] = currentDigit;
        // printf("\tdigits[%d] = %d", i-1, digits[i-1]);
    }

    for (int i = 0; i < numberOfDigits; i++) {
        printf("%d. %d\n", i, digits[i]);
        totalValue += power(digits[i], 2);
    }

    if (totalValue == 1) {
        //reset totalLoops and return happy number found
        totalLoops = 0;
        return true;
    } else {
        if (totalLoops == MAX_LOOPS) {
            return false;
        } else {
            isHappy(totalValue);
        }
    }
    return;
}

int main(void) {
    int number = 3;
    bool happyNumber = false;

    happyNumber = isHappy(number);
    printf("\nNumber %d happy = %s\n", number, happyNumber ? "true" : "false");

    return 0;
}