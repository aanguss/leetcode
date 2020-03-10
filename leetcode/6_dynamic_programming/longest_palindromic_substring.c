/**
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLEN 1000

char * longestPalindrome(char * s) {
    int lenOfS = strlen(s);
    char * pally = malloc(sizeof(char) * lenOfS);
    int possiblePally = 1;
    int k = 0;
    int leftIndex, rightIndex;
    int longestPally = 0;
    int leftPally, rightPally;
    
    // don't start at 0 because there needs to be room to look for pallys
    for (int i = 1; i < lenOfS - 1; i++) {
        // start the possibility over
        possiblePally = 1;

        // if a valid pally is around, let it keep going to find distance
        while (possiblePally != 0 && i - possiblePally >= 0 && i + possiblePally < lenOfS - 1) {
            // get current left and right index numbers
            leftIndex = i - possiblePally;
            rightIndex = i + possiblePally;
            // look for values that match around another number
            if (s[leftIndex] == s[rightIndex]) {            
                // determine if there is a new pally king
                if (rightIndex - leftIndex > longestPally) {
                    leftPally = leftIndex;
                    rightPally = rightIndex;
                    longestPally = rightPally - leftPally;
                }
                possiblePally++;
                // make sure you dont go out of bounds
                // if (i - possiblePally < 0 || i + possiblePally > lenOfS) {
                //     possiblePally = 0;
                //     break;
                // }
            } else {
                possiblePally = 0;
            }
        }
    }

    k = 0;
    // char pally[rightPally - leftPally];
    for (int i = leftPally; i <= rightPally; i++) {
        pally[k] = s[i];
        k++;
    }

    return pally;
}

int main(void) {
    printf("\n");
    char * input = "babad";
    char * output = malloc(sizeof(char) * MAXLEN);

    output = longestPalindrome(input);
    printf("longest palindromic string from %s: %s\n", input, output);

    printf("\n");
    return 0;
}