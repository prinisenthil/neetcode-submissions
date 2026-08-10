class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sums = nums.copy()
        suffix_sums = nums.copy()
        for i in range(len(nums)-2):
            prefix_sums[i+1] *= prefix_sums[i]
        for i in range(len(nums)-1, 1, -1):
            suffix_sums[i-1] *= suffix_sums[i]
        res = []
        for i in range(len(nums)):
            left_val = prefix_sums[i-1] if i-1 >= 0 else 1
            right_val = suffix_sums[i+1] if i+1 < len(suffix_sums) else 1
            res_num = left_val * right_val
            res.append(res_num)

        return res