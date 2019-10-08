class Solution(object):
    def groupAnagrams(self, strs):
        def get_key(str):
            arrs = []
            for s in str:
                arrs.append(s)
            arrs.sort()
            return "".join(arrs)
        index_map = {}
        res = []
        for s in strs:
            key = get_key(s)
            if index_map.has_key(key):
                index_map[key].append(s)
            else:
                index_map[key] = [s]
        for value in index_map.values():
            res.append(value)
        return res


a = Solution()
print a.groupAnagrams(["a"])