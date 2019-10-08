import time
class Solution(object):
    def reverseString(self, s):
        # for i in range(len(s)/2):
        #     s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        return s.reverse()

a = Solution()
arr = []
for i in range(10):
    arr.append(str(i))

for i in range(20):
    arr += arr
start = time.time()
a.reverseString(arr)
print time.time() - start
start = time.time()
a.reverseString(arr)
print time.time() - start
start = time.time()
a.reverseString(arr)
print time.time() - start