/**
 * https://www.pramp.com/challenge/r1Kw0vwG6OhK9AEGAy6L
 * 
 * 
Decode Variations
A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

Examples:

input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
Constraints:

[time limit] 5000ms

[input] string S

1 ≤ S.length ≤ 12
[output] integer
*/
#include <stdio.h>
#include <stdlib.h>
#define MAX_ARR 12

const int decodeVariations(const char *s)
{  
  int len_s = sizeof(s)/sizeof(s[0]);
  int * arr = malloc(sizeof(int) * MAX_ARR);
  //int len_arr = sizeof(arr)/sizeof(arr[0]);
  int numOfDigits = 0;
  int i = 0;
  
	while (i <= len_s -1 ) {
    if(s[i] == 1) {
      //numOfDigits++;
      if(s[i+1] <= 9) {
        numOfDigits++;
        i+=1;
      }
    }
  
    if(s[i] <= 2) {
      //numOfDigits++;
      if(s[i+1] <= 6) {
        numOfDigits++;
        i+=1;
      }
    }
    
    numOfDigits++;
    i++;
    
  }
  
  return numOfDigits;
}

int main() 
{
	return 0;
}