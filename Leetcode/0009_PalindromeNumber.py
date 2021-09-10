class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            return str(x) == str(x)[::-1]
        else:
            return False
        