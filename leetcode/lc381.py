from random import choice

class RandomizedCollection(object):
    class Element(object):
        def __init__(self, val, pos):
            self.val = val
            self.pos = pos
            

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.map = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        map_lst = self.map.get(val)
        if map_lst is None:
            map_lst = self.map[val] = []
        element = self.Element(val, len(self.array))
        self.array.append(element)
        map_lst.append(element)
        return len(map_lst) == 1
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        map_lst = self.map.get(val)
        if map_lst is None:
            return False
        element = map_lst.pop()
        if len(map_lst) == 0:
            del self.map[val]
        # Move self.array[-1] and update the attribute "pos"
        pos = element.pos
        self.array[-1].pos = pos
        self.array[pos] = self.array[-1]
        del self.array[-1]

        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.array).val
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
