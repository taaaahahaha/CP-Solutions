class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        c=0
        m=0
        i=0
        while i<len(s):
            if s[i] in d.keys():
                i=d[s[i]]+1
                if c>m:m=c
                c=0
                d=dict()    
            else:
                d[s[i]]=i
                i+=1
                c+=1
        
        return max(c,m)
                
            
        