/* https://leetcode.com/explore/interview/card/google/63/sorting-and-searching-4/3080/ */
/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * Find the median of the two sorted arrays. The overall run time complexity 
 * should be O(log (m+n)).
 * 
 * You may assume nums1 and nums2 cannot be both empty.
 */
/**
 * Example #1
 * nums1 = [1, 3]
 * nums2 = [2]
 * 
 * The median is 2.0
 */
/** 
 * Example #2
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * 
 * The median is (2 + 3)/2 = 2.5
 */
#include <stdio.h>
#include <stdlib.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    double median1 = 0, median2 = 0;
    for(int i = 0; i < nums1Size; i++) {
        median1 += nums1[i];
    }
    for(int i = 0; i < nums1Size; i++) {
        median2 += nums2[i];
    }
    median1 = median1 / nums1Size;
    median2 = median2 / nums2Size;
    return (median1 + median2) / 2;
}

int main(void) {
    int nums1[2] = {1, 2};
    int nums2[2] = {3, 4};
    double median;
    
    median = findMedianSortedArrays(nums1, sizeof(nums1)/sizeof(nums1[0]),
            nums2, sizeof(nums2)/sizeof(nums2[0]));
    printf("media = %f\n", median);
}