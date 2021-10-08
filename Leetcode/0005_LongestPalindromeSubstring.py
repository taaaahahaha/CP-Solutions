class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        max_len = len(s)
        i = len(s)
        while i>0:
            
            temp = max_len-i+1
            
            for k in range(1,temp+1):
                x = s[k-1:k+i]
                t=x
                if x==t[::-1]:
                    return x
            i-=1
            
            
            