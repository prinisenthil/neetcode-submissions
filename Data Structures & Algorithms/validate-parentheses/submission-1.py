class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        for c in s:
            if c == ")":
                if not openStack:
                    return False
                elif openStack.pop() == "(":
                    continue
                else:
                    return False
            elif c == "}":
                if not openStack:
                    return False
                elif openStack.pop() == "{":
                    continue
                else:
                    return False
            elif c == "]":
                if not openStack:
                    return False
                elif openStack.pop() == "[":
                    continue
                else:
                    return False
            else:
                openStack.append(c)
                continue
        if not openStack:
            return True
        else:
            return False