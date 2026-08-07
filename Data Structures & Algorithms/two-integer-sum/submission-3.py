class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = Counter()
        for i in range(len(nums)):
            hashTable[nums[i]] = i + 1
            print(hashTable[nums[i]])
        for j in range(len(nums)):
            find = target - nums[j]
            print(find)
            i = hashTable[find]
            if hashTable[find] > 0 and i-1 != j:
                i -= 1
                return [min(i,j), max(i,j)]
        return [-1,-1]
