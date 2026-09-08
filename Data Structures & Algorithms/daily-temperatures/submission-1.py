class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                #print(stack, i)
                continue
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
                #print(stack[-1], temperatures[i])
            else:
                #print(temperatures[stack[-1]], temperatures[i])
                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            #print("Stack:",stack)
            #print("Result:",res)
            #print(stack, i)
        return res