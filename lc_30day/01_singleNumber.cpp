
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
#include <map>
#include <algorithm>

using namespace std; 

class Solution {
    map< vector<int>, int > visited;
public:
    // in C this looks like: int singleNumber(int* nums, int numsSize){ ... }
    int singleNumber(std::vector<int>& nums) {
        // map<vector<int>, int> vis;
        

        for_each(nums.begin(), nums.end(), doubleCheck);
        
        // create array size of nums
        // go the numbers and save them in another vector
        // if the number already exists add them to vector
        // 
    }
private:
    void doubleCheck() {

    }
};

int main() {
    Solution solution;
    std::vector <int> myVector = {10, 1, 10, 2, 2};

    solution.singleNumber(myVector);
    return 0;
}