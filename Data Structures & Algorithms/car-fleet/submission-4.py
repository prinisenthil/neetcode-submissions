class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort positions in descending order
        positionSorted = sorted(zip(position, speed), reverse=True)
        # track projected times in stack
        stack = []
        # loop through sorted positions and compare projected target reach time
        # of current car with time of car in front
        for currPosition, currSpeed in positionSorted:
            # get speed and position of current car
            projectedTime = (target - currPosition) / currSpeed
            # initial stack value
            if not stack:
                stack.append(projectedTime)
                continue
            # compare the current car's projected time with car in front
            frontCarProjectedTime = stack[-1]
            if projectedTime <= frontCarProjectedTime:
                continue
            else:
                stack.append(projectedTime)
        return len(stack)
