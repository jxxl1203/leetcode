from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key):
        value = self.dict.get(key)
        if not value:
            return -1
        else:
            self.dict.pop(key)
            self.dict[key] = value
        return value

    def put(self, key, value):
        if self.dict.has_key(key):
            self.dict.pop(key)
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(False)
        return


obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print obj.get(1)
obj.put(3,3)
print obj.get(2)
obj.put(4,4)
print obj.get(1)
print obj.get(3)
print obj.get(4)
