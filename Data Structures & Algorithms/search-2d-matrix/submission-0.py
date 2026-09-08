class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # set l and r rows
        l = 0
        r = len(matrix) - 1
        while (l <= r):
            mid = int((l + r) / 2)
            row = matrix[mid]
            lowest = row[0]
            highest = row[len(row)-1]
            if target <= highest and target >= lowest:
                return self.search(row, target)
            else:
                if target > highest:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    # binary search algo to search rows within matrix
    def search(self, nums: List[int], target: int):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int((l + r) / 2)
            num = nums[mid]
            if target == num:
                return True
            if target > num:
                l = mid + 1
            else:
                r = mid - 1
        return False
