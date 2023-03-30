# Taaha Multani @ https://github.com/taaaahahaha
# Title: 0008_Palindrome.py
# Date: 2023-03-30 08:38:29

ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

# O(len(x)^2)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if str(x) == str(x)[::-1]:
            return True
        return False


# O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        temp = x
        ans = 0

        if x<0:
            return False

        while temp != 0:
            r = temp%10
            temp = temp//10
            ans = (ans * 10) + r
        
        if x == ans:
            return True
        else:
            return False

# O(n/2)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x%10 == 0:
            return False

        temp = x
        ans = 0

        while temp>ans:
            r = temp % 10
            temp = temp // 10
            ans = (ans*10) + r
        print(temp,ans,ans//10)
        if temp == ans or temp == ans//10:
            return True
        return False
