class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find midpoint of the array
        # check target = midpoint
        # if target < midpoint check left half recursively
        # if target > midpoint check right half recursively
        if len(nums) == 1:
            if nums[0] == target:
                return 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int((l+r) / 2)
            num = nums[mid]
            print(mid, num)
            if target == num:
                return mid
            if target < num:
                r = mid-1
            else:
                l = mid+1
        return -1