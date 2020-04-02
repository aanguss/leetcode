
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

#include <iostream> 
#include <vector> 
#include <cstdio>
#include <stdio.h>

using namespace std; 

class Solution {
public:
    // in C this looks like: int singleNumber(int* nums, int numsSize){ ... }
    int singleNumber(vector<int>& nums) {
        printf("test complete");

        return 0;
    }
};

int main() {
    Solution solution;
    vector<int> array_1 {2,2,1};
    vector<int> array_2 {4,1,2,1,2};

    solution.singleNumber(array_1);


    return 0;
}