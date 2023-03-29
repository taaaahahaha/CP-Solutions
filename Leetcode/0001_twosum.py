# Taaha Multani @ https://github.com/taaaahahaha
# Title: 0001_twosum.py
# Date: 2023-03-29 20:29:37

ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

# O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]],i]
            d[nums[i]] = i