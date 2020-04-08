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

#define MAX_DIGITS 10
#define MAX_LOOPS 10000
#define MAX_SEEN 50
int totalLoops = 0;
int seenNumbers[MAX_SEEN];
int currentSeenNumber = 0;

long int power(int base, int exp) {
    long int value = 1;

    for (int i = 0; i < exp; i++) {
        value *= base;
    }

    return value;
}

int getDigit(int num, int pos) {
    return 1;
}

void resetTrackers(void) {
    totalLoops = 0;
    currentSeenNumber = 0;
    for (int i = 0; i < MAX_SEEN; i++) {
        seenNumbers[i] = 0;
    }
}

bool isHappy(int n) {
    int digits[MAX_DIGITS];
    long int currentDigit = 0;
    long int currentRemain = 0;
    int numberOfDigits = 0;
    int totalValue = 0;
    long int num = n;

    while (1) {
        // start over
        for (int i = 0; i < MAX_DIGITS; i++) {
            digits[i] = 0;
        }
        currentDigit = 0;
        currentRemain = 0;
        numberOfDigits = 0;
        totalValue = 0;

        // start recursive loop count and save number to seen list
        totalLoops++;
        printf("\n%d. n = %ld\n", totalLoops, num);
        if (totalLoops == MAX_LOOPS) {
            printf("max loops");
            resetTrackers();
            return false;
        }
        
        
        // end if number already seen
        for (int i = 0; i < currentSeenNumber; i++) {
            printf("\tseenNumbers[%d] = %d\n", i, seenNumbers[i]);
            if (seenNumbers[i] == num) {
                printf("already saw number, seenNumbers[%d] = %d", i, seenNumbers[i]);
                resetTrackers();
                return false;
            }
            // } else {
            //     seenNumbers[i - 1] = n;
            //     break;
            // }
        }
        currentSeenNumber++;
        if (currentSeenNumber == MAX_SEEN) {
            printf("max seen numbers");
            return false;
        } else {
            seenNumbers[currentSeenNumber - 1] = num;
        }
        

        for(int i = 1; i <= MAX_DIGITS; i++) {
            numberOfDigits++;
            currentRemain = num / power(10, i);
            currentDigit = (num % power(10,i)) / power(10, i - 1);

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
            // printf("%d. %d\n", i, digits[i]); // pritn each digit
            totalValue += power(digits[i], 2);
        }

        printf("\ttotalValue = %d", totalValue);

        if (totalValue == 1) {
            //reset totalLoops and return happy number found
            resetTrackers();
            return true;
        } else {
            num = totalValue;
        }
    }

    return false;
}

int main(void) {
    int number = 110935384;
    bool happyNumber = false;
    resetTrackers();

    happyNumber = isHappy(number);
    printf("\nNumber %d is happy? %s\n", number, happyNumber ? "true" : "false");

    return 0;
}