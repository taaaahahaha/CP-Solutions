class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = len(pattern)
        s = [i for i in s.split()]
        print(s)
        i=0
        found = False
        d = {}
        if len(s) != len(pattern):
            return False
        if len(set(s))!=len(set([i for i in pattern])):
            return False
        while i<l and not found:
            if pattern[i] in d.keys():
                if d[pattern[i]]!=s[i]:
                    return False
            else:
                d[pattern[i]]=s[i]
            i+=1
            print(d)
        return True