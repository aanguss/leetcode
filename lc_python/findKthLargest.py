from typing import List
# import typing
class Solution:
    def binarySearchRecursively(self, nums, left, right, val):
        if right >= left:
            middle = (right + left) // 2
            # return if val is in the middle
            if (nums[middle] == val):
                return middle
            # if val is less than middle, search left side of nums
            elif (nums[middle] > val):
                return self.binarySearchRecursively(nums, left, middle - 1, val)
            # if its not less than, it must be greater than, so search right side of nums
            else:
                return self.binarySearchRecursively(nums, middle + 1, right, val)
        # right should be greater than or equal to left otherwise it can't be present
        else:
            return -1
            

    def mergeSort(self, nums):
        if (len(nums) > 1):
            middle = len(nums) // 2
            leftArray = nums[:middle]
            rightArray = nums[middle:]

            # sort left side of nums
            self.mergeSort(leftArray)
            # sort right side of nums
            self.mergeSort(rightArray)
            # merge results
            i = 0
            j = 0
            k = 0
            while (i < len(leftArray) and j < len(rightArray)):
                if (leftArray[i] < rightArray[j]):
                    nums[k] = leftArray[i]
                    i += 1
                else:
                    nums[k] = rightArray[j]
                    j += 1
                k += 1
            # get the remainders from each elements of leftArray
            while (i < len(leftArray)):
                nums[k] = leftArray[i]
                i += 1
                k += 1

            # get the remainder from each elements of rightArray
            while (j < len(rightArray)):
                nums[k] = rightArray[j]
                j += 1
                k += 1


    def findKthLargest(self, nums: List[int], k: int) -> int:

        self.mergeSort(nums)
        # nums.sort()
        # nums.sort(reverse = True)
        print(nums)
        return nums[len(nums) - k]
        # return nums[k - 1]

        # if (len(nums) is 1):
        #     largestNum = nums[0]
        # elif (len(nums) is 2):
        #     if (k == 1):
        #         largestNum = nums[1]
        #     else:
        #         largestNum = nums[0]
        # else:
        #     kIteration = 0
        #     for n in range(len(nums) - 1, -1, -1):
        #         if (n == len(nums) - 1):
        #             largestNum = nums[n]
        #             print(f"starting largest is {largestNum}")
        #             kIteration = 1
        #         else:
        #             if (kIteration == k):
        #                 break
        #             print(f"nums[{n}] = {nums[n]}")
        #             if (nums[n] <= largestNum):
        #                 largestNum = nums[n]
        #                 print(f"largest is now {largestNum}")
        #                 kIteration += 1

        # return largestNum




s = Solution()
nums = [3,2,1,5,6,4]
print(nums)
k = 2
kth = s.findKthLargest(nums,k)
print(f"largest = {kth}")

# nums = [3,2,3,1,2,4,5,5,6]
# print(nums)
# k = 4
# kth = s.findKthLargest(nums,k)
# print(f"largest = {kth}")

# nums = [1,2,1]
# print(nums)
# k = 1
# kth = s.findKthLargest(nums,k)
# print(f"largest = {kth}")

# nums = [1,2]
# print(nums)
# k = 1
# kth = s.findKthLargest(nums,k)
# print(f"largest = {kth}")

# nums = [1,2]
# print(nums)
# k = 2
# kth = s.findKthLargest(nums,k)
# print(f"largest = {kth}")

# nums = [1]
# print(nums)
# k = 1
# kth = s.findKthLargest(nums,k)
# print(f"largest = {kth}")

# nums = [-1,2,0]
# print(nums)
# k = 3
# kth = s.findKthLargest(nums,k)
# print(f"largest = {kth}")

temp = [38, 27, 43, 3, 9, 82, 10]
print(temp)
s.mergeSort(temp)
k = 27
index = s.binarySearchRecursively(temp, 0, len(temp) - 1, k)
print(f"temp[{index}] = {temp[index]}")

# temp = [38, 27, 43, 3, 9, 82, 10]
# print(temp)
# s.mergeSort(temp)
# print(temp)
 
