class MinStack:

    def __init__(self):
        self.elements = []
        self.prefix_arr = []

    def push(self, val: int) -> None:
        self.elements.append(val)
        if len(self.prefix_arr) == 0:
            self.prefix_arr.append(val)
        else:
            if self.prefix_arr[len(self.prefix_arr) - 1] > val:
                self.prefix_arr.append(val)
            else:
                self.prefix_arr.append(self.prefix_arr[len(self.prefix_arr) - 1])

    def pop(self) -> None:
        self.elements.pop(len(self.elements) - 1)
        self.prefix_arr.pop(len(self.prefix_arr) - 1)

    def top(self) -> int:
        return self.elements[len(self.elements) - 1]

    def getMin(self) -> int:
        return self.prefix_arr[len(self.elements) - 1]

        
