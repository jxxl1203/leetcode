from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        begin_queue = [beginWord]
        end_queue = [endWord]
        begin_visited = {beginWord: True}
        end_visited = {endWord: True}
        dict = defaultdict(list)
        l = len(beginWord)

        begin_table = {beginWord:[beginWord]}
        end_table = {endWord:[endWord]}

        for word in wordList:
            for i in range(l):
                dict[word[:i] + '*' + word[i+1:]].append(word)

        res = []
        i = 0
        while begin_queue and end_queue:
            tmp_queue = []
            if res:
                return res
            i += 1
            for b_word in begin_queue:
                for i in range(l):
                    key = b_word[:i] + '*' + b_word[i + 1:]
                    for word in dict[key]:
                        if word in end_visited and word not in begin_visited:
                            tmp = begin_table[b_word] + end_table[word]
                            if res:
                                if len(res[0]) == len(tmp):
                                    res.append(tmp)
                            else:
                                res.append(tmp)
                        if word not in begin_visited:
                            tmp_queue.append(word)
                            begin_visited[word] = True
                            begin_table[word] = begin_table[b_word] + [word]
            begin_queue = tmp_queue

            e_word = end_queue.pop(0)
            tmp_queue = []

            for i in range(l):
                key = e_word[:i] + '*' + e_word[i+1:]
                for word in dict[key]:
                    if word not in end_visited:
                        tmp_queue.append(word)
                        end_visited[word] = True
                        end_table[word] = [word] + end_table[e_word]
            end_queue = tmp_queue
        return res
    ## TODO UNAC



    # def findLadders(self, beginWord, endWord, wordList):
    #     dict = defaultdict(list)
    #     l = len(beginWord)
    #
    #     for word in wordList:
    #         for i in range(l):
    #             dict[word[:i] + '*' + word[i+1:]].append(word)
    #
    #     queue = [(beginWord, [beginWord])]
    #     visited = {}
    #     res = []
    #     while queue:
    #         word, dist = queue.pop(0)
    #         if res and len(dist) >= len(res[0]):
    #             return res
    #         visited[word] = True
    #         for i in range(l):
    #             key = word[:i] + '*' + word[i+1:]
    #             for wd in dict[key]:
    #                 if wd == endWord:
    #                     res.append(dist + [wd])
    #                 if wd not in visited:
    #                     queue.append((wd, dist+[wd]))
    #     return res


a = Solution()
print a.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])