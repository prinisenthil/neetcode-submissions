import operator
class Solution:
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t.strip("-").isnumeric():
                nums.append(int(t))
            else:
                nums[len(nums)-2] = int(self.operations[t](nums[len(nums)-2], nums[len(nums)-1]))
                nums.pop()
        return nums[0]