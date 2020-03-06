/* https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/3081/ */
/**
 * Given an array of integers nums sorted in ascending order, find the
 * starting and ending position of a given target value.
 * 
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * 
 * If the target is not found in the array, return [-1, -1].
 */
/**
 * Example #1
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 */
/**
 * Example #2
 * Input: nums = [5,7,7,8,8,10], target = 6
 * Output: [-1,-1]
 */
#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize) {
    int indexStart = -1;
    int indexEnd = -1;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == target && indexStart == -1) {
            indexStart = i;
        }
        if (nums[i] == target && indexStart != -1) {
            indexEnd = i;
        }
    }
    int * returnArray = malloc(sizeof(int) * *returnSize);
    returnArray[0] = indexStart;
    if (indexStart != -1) {
        if (indexEnd != -1) {
            returnArray[1] = indexEnd;
        } else {
            returnArray[1] = indexStart;
        }
        
    }
    return returnArray;
}

int main(void) {
    int arrayOne[6] = {5,7,7,8,8,10};
    int targetOne = 8;
    int returnSize = 2;
    int * arrayReturn = malloc(sizeof(int) * returnSize);
    arrayReturn = searchRange(arrayOne, sizeof(arrayOne)/sizeof(arrayOne[0]), targetOne, &returnSize);
    // int* searchRange(int* nums, int numsSize, int target, int* returnSize) 
    for (int i = 0; i < returnSize; i++) {
        printf("array[%d] = %d\n", i, arrayReturn[i]);
    }
    free(arrayReturn);
    return 0;
}