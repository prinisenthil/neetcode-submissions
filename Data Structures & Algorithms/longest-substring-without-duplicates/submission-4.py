class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        letterDict = {}
        max_len = 0
        start = 0
        i = 0

        while i < len(s):
            c = s[i]
            if c in letterDict and letterDict[c] >= start and letterDict[c] < i:
                if (i - start) > max_len:
                    max_len = i - start
                start = letterDict[c] + 1
                letterDict[c] = i
            else:
                letterDict[c] = i
            i += 1
        if (i - start) > max_len:
            max_len = i - start
        return max_len
            
                

        