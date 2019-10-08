# coding=utf-8
# 超时
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         self.res = float('inf')
#         def _helper(word, list, times):
#             if times > self.res:
#                 return
#             if word == endWord:
#                 self.res = min(self.res, times)
#             if len(list) == 0:
#                 return
#             for i in range(len(list)):
#                 if can_use(word, list[i]):
#                     # print word, list[i], times+1
#                     _helper(list[i], list[:i]+list[i+1:], times+1)
#
#         def can_use(word, target):
#             times1, times2, diff = 0, 0, 0
#             for i in range(len(word)):
#                 if word[i] != target[i]:
#                     diff += 1
#                 if diff > 1:
#                     return False
#                 if word[i] == endWord[i]:
#                     times1 += 1
#                 if target[i] == endWord[i]:
#                     times2 += 1
#
#             return diff == 1 and times1 <= times2
#
#         _helper(beginWord, wordList, 1)
#         return self.res if self.res != float('inf') else 0


# from collections import defaultdict
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         word_dict = defaultdict(list)
#         visited = {}
#         l = len(beginWord)
#         for word in wordList:
#             for i in range(l):
#                 word_dict[word[:i] + '*' + word[i+1:]].append(word)
#
#         queue = [(beginWord, 1)]
#         while queue:
#             block = queue.pop(0)
#             wd = block[0]
#             visited[wd] = True
#             dist = block[1]
#             for i in range(l):
#                 key = wd[:i] + '*' + wd[i+1:]
#                 for word in word_dict[key]:
#                     if word == endWord:
#                         return dist + 1
#                     if not visited.has_key(word):
#                         queue.append((word, dist+1))
#         return 0
#



from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        self.l = len(beginWord)
        # if not beginWord or not endWord or endWord not in wordList:
        #     return 0
        self.dict = defaultdict(list)
        for word in wordList:
            for i in range(self.l):
                self.dict[word[:i] + '*' + word[i+1:]].append(word)
        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]
        visited_begin = {beginWord:1}
        visited_end = {endWord:1}
        while queue_end and queue_begin:
            res = self._helper(queue_begin, visited_begin, visited_end)
            if res != 0:
                return res

            res = self._helper(queue_end, visited_end, visited_begin)
            if res != 0:
                return res
        return 0


    def _helper(self, queue, visited, other_visited):
        word, dist = queue.pop(0)
        visited[word] = dist
        for i in range(self.l):
            key = word[:i] + '*' + word[i+1:]
            for ws in self.dict[key]:
                if ws in other_visited:
                    return dist + other_visited[ws]
                if ws not in visited:
                    queue.append((ws, dist+1))
                    visited[ws] = dist + 1
        return 0


a = Solution()
print a.ladderLength("lost", "cost",["most","fist","lost","cost","fish"])
# print a.ladderLength("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
"lost"
"cost"
["most","fist","lost","cost","fish"]