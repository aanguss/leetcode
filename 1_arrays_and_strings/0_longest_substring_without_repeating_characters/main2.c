#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * @brief get substring from index start and stop
 * @param string - string to pull substring from
 * @param iStart - starting index 
 * @param iStop - stopping index
 * @return substring requested
 */
// char * getSubstring(char * string, int iStart, int iStop) {
//     // char * subString = NULL;
//     // char currentChar = NULL;
    
//     // go through string to get substring from indexes
//     // for (int i = 0; i < strlen(string); i++) {
        
//     // }

// }

/**
 * @brief given a string, return longest non-repeating string
 * @param s - string to search through
 * @return length of longest string
 */
int lengthOfLongestSubstring(char * s) {
    char * longString = malloc(sizeof(*s));
    char * longestString = malloc(sizeof(*s));
    char firstChar = *s;
    memcpy(longestString, s, 1);
    // longestString = firstChar;
    int lenS = strlen(s);
    int lenLS = 0;
    int startIndex = -1, endIndex = 0;
    int i,j;
    int stringLen = 0;

    // longString = &s[0]+1;
    // longString = s;
    // printf("longString = %s", longString);

    // print start string
    printf("parsing string %s\n", s);

    // find start and end of repeated character
    for (i = 0; i < lenS; i++) {
        for (j = i+1; j < lenS; j++) {
            if (s[i] == s[j]) {
                printf("\nfound %c @ (i=%d,j=%d)\n", s[i], i, j);
                // startIndex = i;
            // get substring
            // stringLen = j-i-1;
            printf("string length = %d\n", j-i);
            printf("staring of string = %c\n", s[i]);
            printf("end of string = %c\n", s[j]);
            // strncat(longString, &(s[i]), stringLen);
            // strncpy(longString, s[i], stringLen);
            memcpy(longString, &s[i], j-i);
               break;
            }
            // // strncat(longestString, &s[j], 1);
            printf("substring = %s, with length %ld\n", longString, strlen(longString));

            // compare length of new substring and current longest string
            // lenLS = strlen(longestString);
            printf("longestString length = %ld\n", strlen(longestString));
            if (strlen(longString) > strlen(longestString))
            {
                longestString = longString;
                printf("-->found longer string %s\n", longestString);
            }
        }
    }

    printf("-->LONGEST string %s\n", longestString);


    // if (startIndex = -1) {
    //     startIndex = 0;
    // }

    // find end index
    // for (i = startIndex; i < lenS; i++) {
    //     for (j = i+1; j < lenS; j++) {
    //         if (s[i] == s[j]) {
    //             printf("found start index %d @ (i=%d,j=%d)\n", startIndex, i, j);
    //             startIndex = i;
    //         }
    //     }
    // }
    
}

int main(void){
    char * example1 = "abcabcbb";
    char * example2 = "bbbb";
    char * example3 = "pwwkew";

    printf("\nexample 1:");
    lengthOfLongestSubstring(example1);

    printf("\nexample 2:");
    lengthOfLongestSubstring(example2);

    printf("\nexample 3:");
    lengthOfLongestSubstring(example3);

    // char *s = "this is a test";

    // char *p = s;
    // while (*p != '\0'){
       
    //     char c = *p;
    //     p++;
    //     printf("%c\n",c);
    // }

    return 0;
}