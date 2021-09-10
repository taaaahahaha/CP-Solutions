class Solution:
    
    def twoSum(self, nums, target):
            values = {}
            for i, num in enumerate(nums):
                remaining = target - num
                if remaining in values:
                    return [i, values[remaining]]
                else:
                    values[num] = i
     