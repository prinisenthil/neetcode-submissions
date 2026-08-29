class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights[0], heights[1])
        start = 0
        end = len(heights) - 1
        max_area = 0
        while start < end:
            h1 = heights[start]
            h2 = heights[end]
            curr_area = min(h1, h2) * (end - start)
            if curr_area > max_area:
                max_area = curr_area
            if min(heights[start], heights[end]) == heights[start]:
                start += 1
            else:
                end -= 1
            #print(start, end)
        return max_area