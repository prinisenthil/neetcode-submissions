class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        longest = 0
        for num in nums:
            if num-1 in hashSet:
                continue
            start = num
            currentLen = 1
            while start+1 in hashSet:
                currentLen += 1
                start += 1
            if longest < currentLen:
                longest = currentLen
        return longest