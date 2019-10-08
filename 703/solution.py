import random, time

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.k = k
        self.heap = []
        for i in range(max(0,len(nums) - k), len(nums)):
            self.heap.append(nums[i])

    def add(self, val):
        if len(self.heap) < self.k:
            self.heap.insert(0, val)
            self.min_heap(0, len(self.heap))
        elif val > self.heap[0]:
            self.heap[0] = val
            self.min_heap(0, self.k)
        return self.heap[0]

    def min_heap(self, index, length):
        left = index * 2 + 1
        right = index * 2 + 2
        if left > length - 1:
            return
        min = left
        if right < length and self.heap[right] < self.heap[left]:
            min = right
        if self.heap[min] > self.heap[index]:
            return
        self.heap[min], self.heap[index] = self.heap[index], self.heap[min]
        self.min_heap(min, length)

# class KthLargest(object):
#
#     def __init__(self, k, nums):
#         nums.sort()
#         self.nums = []
#
#         for i in range(max(0, len(nums) - k), len(nums)):
#             self.nums.append(nums[i])
#
#         self.k = k
#         self.nums.sort()
#
#     def add(self, val):
#         if len(self.nums) < self.k:
#             self.nums.append(val)
#         elif self.nums[0] < val:
#             self.nums[0] = val
#         self.nums.sort()
#         return self.nums[0]

nums = []
for i in range(9999):
    nums.append(random.randint(1, 10000))
a = KthLargest(9999, nums)

begin = time.time()
for i in range(10000):
    # start = time.time()
    a.add(random.randint(1, 10000))
    # print "add %s finish use %s " % (i, time.time() - start)
print "total time %s" % (time.time() - begin)
print a.heap
# a = KthLargest(373,[4,5,8,2])
# print a.add(373)
# print a.add(5)
# print a.add(10)
# print a.heap
# print a.add(9)
# print a.heap
# print a.add(4)
