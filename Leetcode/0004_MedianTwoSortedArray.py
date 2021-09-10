class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1+nums2
        num.sort()
        l = len(num)
        print(l,num)
        if l%2==0:
            median = (num[l//2]+num[l//2-1])/2
        else:
            median = num[l//2]
        return median