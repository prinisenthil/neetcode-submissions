class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable = Counter()
        for letter in s:
            hashTable[letter] += 1
        for letter in t:
            if hashTable[letter] >= 1:
                hashTable[letter] -= 1
            else:
                return False
        for letter in s:
            if hashTable[letter] != 0:
                return False
        return True
            