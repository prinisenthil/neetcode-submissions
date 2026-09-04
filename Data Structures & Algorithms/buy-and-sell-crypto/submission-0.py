class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        max_profit = 0
        min_left_arr = [0] * len(prices)
        max_right_arr = [0] * len(prices)
        for i in range(len(prices)):
            j = len(prices) - 1 - i
            if i == 0:
                min_left_arr[0] = prices[0]
                max_right_arr[j] = prices[j]
                continue
            if prices[i] < min_left_arr[i-1]:
                min_left_arr[i] = prices[i]
            else:
                min_left_arr[i] = min_left_arr[i-1]
            if prices[j] > max_right_arr[j+1]:
                max_right_arr[j] = prices[j]
            else:
                max_right_arr[j] = max_right_arr[j+1]
        
        for i in range(len(prices)):
            diff = max_right_arr[i] - min_left_arr[i]
            if diff > max_profit:
                max_profit = diff
        print(min_left_arr, max_right_arr)
        return max_profit
        
        
            

