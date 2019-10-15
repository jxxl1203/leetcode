# class TrieNode(object):
#     isStr = False
#     children = []
#     def __init__(self):
#         self.children = [None] * 26
#
# class Trie(object):
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         root = self.root
#         for c in word:
#             i = ord(c) - ord('a')
#             if root.children[i]:
#                 root = root.children[i]
#             else:
#                 root.children[i] = TrieNode()
#                 root = root.children[i]
#
#         root.isStr = True
#
#     def search(self, word):
#         root = self.root
#         for c in word:
#             i = ord(c) - ord('a')
#             if root.children[i]:
#                 root = root.children[i]
#             else:
#                 return False
#         return root.isStr
#
#     def startsWith(self, prefix):
#         root = self.root
#         for c in prefix:
#             i = ord(c) - ord('a')
#             if root.children[i]:
#                 root = root.children[i]
#             else:
#                 return False
#         return True


class Trie(object):
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = '#'

    def search(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return '#' in trie

    def startsWith(self, prefix):

        trie = self.trie
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]
        return True

obj = Trie()
obj.insert("apple")
obj.insert("application")
obj.insert("banana")
print obj.search("app")
print obj.search("apple")
print obj.search("ban")
print obj.search("banana")
print obj.startsWith("appc")
print obj.startsWith("appl")
print obj.startsWith("ban")
