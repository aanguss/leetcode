#include <stdio.h>
#include <string.h>
/**
 * @brief function to find length of longest substring that
 *          does not repeat characters
 * @param[in] char * s string to determine
 * @param[out] int length of longest substring
 */
int lengthOfLongestSubstring(char * s){
    int lenOfS = strlen(s);
    char longestString[lenOfS];
    int lenOfLongString = strlen(longestString);
    char * pLongestString = longestString;
    int lols_index = 0;
    int foundRepeat;
    int startIndex;
    int endIndex;
    int i,j;
    int longestIndex = 0;
    printf("found string: %s of length: %d and ls = %d\n", 
            s, lenOfS, strlen(longestString));
    for (i = 0; i <= lenOfS; i++) {
        foundRepeat = 0;
        for (j = i+1; j <= lenOfS; j++) {
            if (s[i] == s[j])
            {
                printf("found repeat, i=%d=%c, j=%d=%c\n",
                    i,s[i],j,s[j]);
                foundRepeat = 1;
                break;
            }
        }
        if (foundRepeat == 0){
            startIndex = i;
        }
    }

    for (i = startIndex+1; i <= lenOfS; i++) {
        foundRepeat = 0;
        for (j = startIndex; j <= lenOfS; j++) {
            if (s[i] == s[j])
            {
                foundRepeat = 1;
                break;
            }
        }
        if (foundRepeat == 1){
            endIndex = i;
        }
    }

    printf("found, startIndex: %d, endIndex: %d", 
            startIndex, endIndex);
    
    for (j = startIndex; j <= endIndex; j++) {
        longestString[lols_index++] = s[j];
    }
    
    // printf("longestString = %s\n", (char*)(&pLongestString[0]));
    printf("longestString = %s\n", longestString);
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

    return 0;
}