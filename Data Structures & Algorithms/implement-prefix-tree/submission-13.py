class TreeNode:
    def __init__(self, val=None, end=False):
        self.val = val
        self.children = {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        prefix = ""
        curr = self.root
        for i, c in enumerate(word):
            prefix += c
            childs = curr.children
            if prefix not in childs:
                childs[prefix] = TreeNode(prefix, i==(len(word)-1))
                #print(prefix, childs[prefix].end)
            elif not childs[prefix].end and i == (len(word)-1):
                childs[prefix].end = True
                #print(prefix, childs[prefix].end)
            curr = childs[prefix]
        

    def search(self, word: str) -> bool:
        curr = self.root
        prefix = ""
        for i, c in enumerate(word):
            prefix += c
            #print(i, prefix)
            if prefix not in curr.children:
                #print(prefix, curr.children)
                return False
            if i == len(word)-1 and not curr.children[prefix].end:
                return False
            curr = curr.children[prefix]
        return True

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        pre = ""
        for c in prefix:
            pre += c
            if pre not in curr.children:
                return False
            curr = curr.children[pre]
        return True
        
        