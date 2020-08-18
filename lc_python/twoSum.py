from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sumList = []

        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                if (nums[a] + nums[b] == target):
                    print(f"{nums[a]} + {nums[b]} = {target}")
                    return ([a, b])
        return []



s = Solution()
nums = [2, 7, 11, 15]
target = 9
print("twoSum of {0} with a target of {1} is {2}".format(nums, target, s.twoSum(nums, target)))