class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        prefix_arr = [0] * len(height)
        suffix_arr = [0] * len(height)
        for i in range(len(height)):
            j = len(height) - i - 1
            if i == 0:
                prefix_arr[0] = height[0]
                suffix_arr[j] = height[j]
                continue
            if height[i] > prefix_arr[i-1]:
                prefix_arr[i] = height[i]
            else:
                prefix_arr[i] = prefix_arr[i-1]
            if height[j] > suffix_arr[j+1]:
                suffix_arr[j] = height[j]
            else:
                suffix_arr[j] = suffix_arr[j+1]
        water_area = 0
        for i in range(len(height)):
            water_area += min(prefix_arr[i], suffix_arr[i]) - height[i]
        return water_area