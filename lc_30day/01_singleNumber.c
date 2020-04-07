
/**
 * https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3283/
 * 
 * Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 * 
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 * 
 * Example 1:
 * Input: [2,2,1]
 * Output: 1
 * 
 * Example 2:
 * Input: [4,1,2,1,2]
 * Output: 4
 */

#include <stdio.h>
#include <gmodule.h>
#include <glib.h>

typedef struct {
    int value;
    int seen;
} numberList_t;

int singleNumber(int* nums, int numsSize) {
    // int fNums[numsSize];// = { 0 }; // all elements 0
    // numberList_t fNums[numsSize];
    int fNums[numsSize];

    for (int i = 0; i < numsSize; i++) {
        fNums[i] = -1;
    }

    printf("\n");

    for(int i = 0; i < numsSize; i++) {
        // printf("%d ", fNums[i]);
        if (fNums[i] == -1) {
            fNums[i] = nums[i];
        }
    }

    for (int i = 0; i < numsSize; i++) {
        if (fNums[])
    }

    printf("\n");
}
 
int main() {
    int blah[5] = {1, 10, 1, 5, 10};
    int sBlah = sizeof(blah) / sizeof(int);
    int singleNum;

    singleNum = singleNumber(blah, sBlah);
    printf("single number = %d", singleNum);

    return 0;
}