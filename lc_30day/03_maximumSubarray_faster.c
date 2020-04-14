/**
 * https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3285/
 * Maximum Subarray
 * 
 * Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
 * 
 * Example:
 * 
 * Input: [-2,1,-3,4,-1,2,1,-5,4],
 * Output: 6
 * Explanation: [4,-1,2,1] has the largest sum = 6.
 * Follow up:
 * 
 * If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 */
#include <stdlib.h>
#include <stdio.h>

int maxSubArray(int * nums, int numsSize) {
    int totalValue = 0;
    int maxValue = nums[0];
    int minLeft = 0;
    int maxRight = 0;
    
    if (numsSize > 1) {
        for (int i = 0; i < numsSize; i++) {
            totalValue = nums[i];
            if (totalValue > maxValue) {
                maxValue = totalValue;
            }
            printf("int i = %d\n", i);
            for (int j = i + 1; j < numsSize; j++) {
                totalValue += nums[j];
                if (totalValue > maxValue) {
                    maxValue = totalValue;
                    minLeft = i;
                    maxRight = j;
                    printf("new (%d -> %d = %d\n", minLeft, maxRight, maxValue);
                }
            }
            printf("\n");
        }
    }

    return maxValue;
}

int main(void) {
    int numbers[9] = {-2,1,-3,4,-1,2,1,-5,4};
    // int numbers[2] = {-2,1};
    // int numbers[2] = {1,2};
    // int numbers[2] = {-2,-1};
    int numbersSize = sizeof(numbers) / sizeof(int);
    int maxNumbers;

    maxNumbers = maxSubArray(numbers, numbersSize);
    printf("Max = %d\n", maxNumbers);

    return 0;
}