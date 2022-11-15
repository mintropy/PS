"""
Title : Implement Trie (Prefix Tree)
Link : https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class Node:
    def __init__(self, s: str = "") -> None:
        self.value = s
        self.word_end = False
        self.childs = dict()


class Trie:
    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        node = self.trie
        for s in word:
            if s not in node.childs:
                node.childs[s] = Node(s)
            node = node.childs[s]
        node.word_end = True

    def search(self, word: str) -> bool:
        node = self.trie
        for s in word:
            if s not in node.childs:
                return False
            node = node.childs[s]
        if node.word_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for s in prefix:
            if s not in node.childs:
                return False
            node = node.childs[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    pass
