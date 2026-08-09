class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "-1" + "#"
        res = ""
        for string in strs:
            num = len(string)
            res = res + str(num) + "#" + string
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        if s == "-1#":
            return []
        if s == "":
            return [""]
        is_number = True
        num = ""
        res_string = ""
        res = []
        for c in s:
            if is_number:
                if c == "#":
                    is_number = False
                    print(num)
                    num = int(num)
                    if num == 0:
                        res.append("")
                        is_number = True
                        num = ""
                    continue
                num += c
            else:
                res_string += c
                num -= 1
                if num == 0:
                    is_number = True
                    res.append(res_string)
                    res_string = ""
                    num = ""
        return res

